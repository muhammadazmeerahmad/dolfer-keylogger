Keylogger Project
Overview
This project is a Python-based keylogger designed for educational purposes. It records keystrokes, saves the data in a local file, and sends periodic keylog reports via email. The application is designed to run silently in the background and can be compiled into an executable file for easy deployment.

Features:
Keystroke Logging: Captures keystrokes and saves them in keylog.txt.

Email Reports: Sends captured logs to a specified email every 2 minutes.

Session Management: Logs the start and end of each session.

Background Operation: Runs silently in the background after being compiled to .exe.

Persistence: Optionally configure auto-start on system boot via the registry (Windows).

Ethical Disclaimer:
This keylogger is for educational purposes only. Unauthorized use or deployment without consent is illegal and unethical. Always obtain explicit permission before using any keylogging software.

Installation
Follow the steps below to get the keylogger running on your system.

Prerequisites:
Python 3.6+

pip (Python's package manager)

Step 1: Clone the Repository
Clone or download the repository to your local machine:

bash
Copy
Edit
git clone https://github.com/yourusername/keylogger-project.git
cd keylogger-project
Dependencies Installation
To install the required dependencies for your platform, follow the instructions for Windows or Linux:

Windows
Open Command Prompt or PowerShell.

Navigate to the project directory.

Run the following command to install dependencies:

bash
Copy
Edit
python -m pip install -r requirements.txt
This will install all the necessary dependencies for your keylogger project.

Linux
Open Terminal.

Navigate to the project directory.

Run the following command to install dependencies:

bash
Copy
Edit
python3 -m pip install -r requirements.txt
Creating the Executable File
You can compile the keylogger project into an executable file using PyInstaller. This will allow you to run the keylogger on any system without needing Python installed.

Step 1: Install PyInstaller
Windows:

bash
Copy
Edit
python -m pip install pyinstaller
Linux:

bash
Copy
Edit
python3 -m pip install pyinstaller
Step 2: Compile the Keylogger Script
Once PyInstaller is installed, you can create an executable file:

Navigate to the project directory.

Run the following command to create an executable:

bash
Copy
Edit
pyinstaller --onefile keylogger.py
This will create a single .exe file for Windows or a single binary for Linux in the dist/ directory.

Running the Keylogger
Windows
To run the keylogger, simply double-click the .exe file generated in the dist/ directory. You can optionally configure it to run automatically on system startup by editing the Windows registry.

Linux
To run the keylogger on Linux, navigate to the dist/ directory and execute the file:

bash
Copy
Edit
./keylogger
Notes
Make sure to change the email and time interval in the keylogger.py before using it.

Never use this tool for malicious purposes. Always get proper consent before using keyloggers.

Use responsibly and within ethical guidelines.

Example Bash Script for Dependency Installation (Windows & Linux)
To automate the installation of dependencies for both Windows and Linux, you can use the following bash script (install_dependencies.sh). This script checks the system and installs the correct dependencies accordingly:

bash
Copy
Edit
#!/bin/bash

# Check if Python is installed
if command -v python3 &>/dev/null; then
    echo "Python 3 detected!"
    PYTHON="python3"
else
    echo "Python 3 not found. Please install Python 3 first."
    exit 1
fi

# Install pip if not installed
if ! command -v pip &>/dev/null; then
    echo "Pip not found, installing pip..."
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    $PYTHON get-pip.py
fi

# Install dependencies from requirements.txt
echo "Installing dependencies..."
$PYTHON -m pip install --upgrade pip
$PYTHON -m pip install -r requirements.txt

echo "Dependencies installed successfully!"
Usage:
Save the script as install_dependencies.sh in the project root.

Make it executable:

bash
Copy
Edit
chmod +x install_dependencies.sh
Run the script:

bash
Copy
Edit
./install_dependencies.sh
This script will automatically detect your system and install the required dependencies.

Troubleshooting
Windows Defender: If Windows Defender detects the .exe file, you may need to add an exception to allow it to run. Be aware that keyloggers are often flagged by antivirus software.

Dependencies Issues: If you encounter issues with dependencies, try upgrading pip and then reinstalling the dependencies:

bash
Copy
Edit
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Conclusion
The Keylogger project is designed for educational use and can be deployed both on Windows and Linux. Be sure to use it responsibly and always within legal and ethical boundaries.
