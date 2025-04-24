# Keylogger Project

## 📝 Overview

This is a **Python-based keylogger** developed strictly for **educational purposes**. It captures user keystrokes, stores them in a local file, and periodically sends logs via email. The tool can be compiled into an executable and is designed to operate in the background silently.

> ✅ **Undetectable by Windows Defender as of 24/04/2025**

---

## ⚙️ Features

- 🧠 **Keystroke Logging** – Saves keystrokes into `keylog.txt`
- 📧 **Email Delivery** – Sends keystroke logs to email every 2 minutes
- 🕵️‍♂️ **Background Operation** – Runs quietly after being compiled to `.exe`
- 🗂️ **Session Tracking** – Logs start and end of each session
- 🔁 **Persistence (optional)** – Can be configured to auto-start on Windows boot

---

## ⚠️ Disclaimer

This keylogger is intended **only for educational and ethical use**. Unauthorized use is **illegal**. You **must obtain permission** from the system owner before use.

---

## 🚀 Installation

### Prerequisites
- Python 3.6 or above
- `pip` installed

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/keylogger-project.git
cd keylogger-project

# 🖥️ Python Keylogger

A lightweight, educational Python-based keylogger for monitoring keystrokes, logging them locally, and optionally sending them via email in real-time.

> ⚠️ **Undetectable by Windows Defender as of 24/04/2025**

---

## 📌 Features

- 🎯 Keystroke logging to `keylog.txt`
- 📧 Email reports sent every 2 minutes
- 🔒 Session management with start/end markers
- 👻 Background operation (runs silently)
- 🔁 Optional persistence via Windows Registry
- 💻 Works on **both Windows and Linux**

---

## ⚠️ Disclaimer

> This project is strictly for **educational and ethical use only**. Unauthorized usage or deployment without consent is illegal and unethical. Obtain proper permissions before usage.

---

## 📦 Dependency Installation

### ✅ Automatic Script (Linux & Windows)

Save the following as `install_dependencies.sh`:

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

echo "📦 Installing dependencies..."
$PYTHON -m pip install --upgrade pip
$PYTHON -m pip install -r requirements.txt
echo "✅ Dependencies installed successfully!"

