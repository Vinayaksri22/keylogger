# keylogger
A keylogger is software that is used to record every single keystroke made by the user on a system using his or her keyboard device. It helps to know which keys were pressed and are actively used today to actively monitor the user activity.

Keystroke Logging Definition
The concept of a keylogger breaks down into two definitions:

Keystroke logging: Record-keeping for every key pressed on your keyboard.
Keylogger tools: Devices or programs used to log your keystrokes.

Keystroke logging is an act of tracking and recording every keystroke entry made on a computer, often without the permission or knowledge of the user. A “keystroke” is just any interaction you make with a button on your keyboard.

Keystrokes are how you “speak” to your computers. Each keystroke transmits a signal that tells your computer programs what you want them to do.

These commands may include:

Length of the keypress
Time of keypress
Velocity of keypress
Name of the key used
When logged, all this information is like listening to a private conversation. You believe you’re only “talking” with your device, but another person listened and wrote down everything you said. With our increasingly digital lives, we share a lot of highly sensitive information on our devices.

User behaviors and private data can easily be assembled from logged keystrokes. Everything from online banking access to social security numbers is entered into computers. Social media, email, websites visited, and even text messages sent can all be highly revealing.

Keylogger tools can either be hardware or software meant to automate the process of keystroke logging. These tools record the data sent by every keystroke into a text file to be retrieved at a later time. Some tools can record everything on your copy-cut-paste clipboard, calls, GPS data, and even microphone or camera footage.

Keyloggers are a surveillance tool with legitimate uses for personal or professional IT monitoring. Some of these uses enter an ethically questionable grey area. However, other keylogger uses are explicitly criminal.

Regardless of the use, keyloggers are often used without the user’s fully aware consent and keyloggers are used under the assumption that users should behave as normal.

How It Works

Frontend:

The webpage captures keystrokes from a textarea element using JavaScript's keydown event.
Each keystroke is sent to the server in real-time using fetch.

Backend:

A Flask app collects the keystrokes via the /collect endpoint.
Logs are accumulated and sent via email when a certain threshold is reached (e.g., 50 characters).

Email Sending:

The send_email function sends the log to the specified email address using SMTP.
