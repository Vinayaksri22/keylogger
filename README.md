# keylogger
A keylogger is software that is used to record every single keystroke made by the user on a system using his or her keyboard device. It helps to know which keys were pressed and are actively used today to actively monitor the user activity.
How It Works
Frontend:

The webpage captures keystrokes from a textarea element using JavaScript's keydown event.
Each keystroke is sent to the server in real-time using fetch.

Backend:

A Flask app collects the keystrokes via the /collect endpoint.
Logs are accumulated and sent via email when a certain threshold is reached (e.g., 50 characters).

Email Sending:

The send_email function sends the log to the specified email address using SMTP.
