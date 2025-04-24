#!/bin/bash

echo "📄 Generating README.md..."

cat << 'EOF' > README.md
# 🖥️ Python Keylogger

A stealthy keylogger built with Python — created for **educational and ethical** purposes only.

---

## ⚙️ Features

- ⌨️ Logs all keystrokes silently
- 📨 Sends keylogs via email every 2 minutes
- 🧾 Saves all data locally in `keylog.txt`
- 🎯 Session Start and End markers
- 🛡️ Currently undetected by Windows Defender (as of 24/04/2025)
- 🔁 (Optional) Persistence via Registry on Windows
- 📦 Compilable to `.exe` using PyInstaller
- 💡 Works on both Windows and Linux

---

## ⚠️ Ethical Disclaimer

> This tool is **strictly for educational and authorized use** only.  
> Unauthorized surveillance or use without permission is **illegal** and **unethical**.

---

## 📦 Dependency Installation

### ✅ Automatic Script (Linux & Windows)

Save and run the following:

```bash
#!/bin/bash

if command -v python3 &>/dev/null; then
    PYTHON="python3"
elif command -v python &>/dev/null; then
    PYTHON="python"
else
    echo "Python is not installed. Please install Python 3 first."
    exit 1
fi

echo "Installing dependencies..."
$PYTHON -m pip install --upgrade pip
$PYTHON -m pip install -r requirements.txt
echo "✅ Dependencies installed successfully!"
