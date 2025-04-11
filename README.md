Overview
This is a Python-based keylogger project that captures keystrokes from the target system, stores the data locally in a text file, and sends the captured logs via email at regular intervals.

Features:
Captures all keystrokes.

Saves logs in keylog.txt.

Sends keylog reports to your email every 2 minutes.

Automatically runs in the background (once converted to .exe).

Can be set to auto-start on Windows boot (optional).

Dependencies:
This project requires the following Python libraries:

pynput – To capture keyboard events.

pyinstaller – To convert the script into an executable.

yagmail – To send emails securely via Gmail.

keyring – For securely handling Gmail credentials.

Install Dependencies:
To install the required dependencies, run the following command:

bash
Copy
Edit
pip install -r requirements.txt
How to Run:
Clone or download this repository to your local machine.

Install dependencies by running the pip install -r requirements.txt command.

Run the keylogger script using Python:

bash
Copy
Edit
python keylogger.py
The keylogger will now capture keystrokes and save them in keylog.txt and send an email every 2 minutes.

Converting to .exe:
To convert the script to a standalone .exe file, use PyInstaller:

bash
Copy
Edit
pyinstaller --onefile --noconsole --icon=icon.ico keylogger.py
This will create a .exe file that you can run on any Windows machine.

Auto-Start on Windows Boot:
If you want the keylogger to run automatically on Windows startup, use the following approach:

Create a file add_to_startup.py that adds the keylogger to the registry.

When the .exe file is executed, it will copy itself to AppData and add a registry entry to start automatically on boot.

Important: Ensure you only use this project ethically and with permission. Unauthorized use of keyloggers is illegal and unethical.

Ethical Note:
This keylogger project is for educational purposes only. Unauthorized use of keyloggers without consent is illegal and unethical. Always ensure that you have proper permission before using such software.

License:
This project is open-source, and you are welcome to modify it for your educational purposes. Please do not use it for malicious activities.

