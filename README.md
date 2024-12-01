# DevDock Package Manager 🚀

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)
[![ADB](https://img.shields.io/badge/ADB-Required-brightgreen.svg)](https://developer.android.com/studio/command-line/adb)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

DevDock Package Manager is a command-line tool for managing apps on Android devices using **Android Debug Bridge (ADB)**. It simplifies tasks like listing, searching, launching, and uninstalling apps directly from your terminal.

---

## Features ✨
- **List Installed Apps:** Displays all packages installed on your Android device.
- **Search Packages:** Search for specific packages by name.
- **Launch Apps:** Open an app on your device directly from the terminal.
- **Uninstall Apps:** Remove user or system apps (requires appropriate permissions).
- **User-Friendly Interface:** Menu-driven UI with clear options and feedback.

---

## Requirements 🛠️
- **Python**: Version 3.6 or higher.
- **ADB**: Installed and configured on your system.
- **USB Debugging**: Enabled on your Android device.

---

## Installation 📥
1. Clone the repository:
   ```bash
   git clone https://github.com/your-profile/adb-package-manager.git
   cd adb-package-manager
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure ADB is installed and added to your system PATH:
   - Download from [Android Developer Tools](https://developer.android.com/studio/command-line/adb).
   - Verify installation with:
     ```bash
     adb version
     ```

---

## Usage 🚦
1. Run the script:
   ```bash
   python adb_package_manager.py
   ```
2. Follow the menu prompts to interact with your connected Android device.

---

## Menu Options 📋
1. **List All Packages**: Displays all installed app packages on your device.
2. **Search for a Package**: Search for specific app packages by name and interact with them.
3. **Uninstall a Package**: Remove user apps by entering the package name.
4. **Uninstall a System App (user 0)**: Uninstall system apps for the default user (requires root or elevated privileges).
5. **About**: View information about the tool and developer.
6. **Exit**: Close the program.

---

## How It Works ⚙️
- **Device Detection**: The script uses `adb devices` to check connected devices.
- **Package Management**: Interacts with the Android package manager (`pm list packages`) via ADB commands.
- **App Actions**: Execute commands like `adb shell monkey` to launch apps and `adb uninstall` to remove them.

---

## Interface 📸
```
Checking for connected devices...

Connected device: SM-T385

==================================================
DevDock Package Manager | Connected Device: SM-T385
==================================================

1. List all packages
2. Search for a package
3. Uninstall a package
4. About
5. Exit

==================================================

Enter your choice:
```
---

## Notes 📝
- Ensure **USB Debugging** is enabled on your Android device.
- For uninstalling system apps, root access may be required.
- Use the tool responsibly to avoid removing critical system packages.

---

## Contributing 🤝
Contributions are welcome! Feel free to fork the repository and submit a pull request.

---

## License 🛡️
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## Developer 💻
- **Sidharth Prabhu**
- GitHub: [https://github.com/Sidharth-Prabhu](https://github.com/Sidharth-Prabhu)
- Version: 1.0
```
