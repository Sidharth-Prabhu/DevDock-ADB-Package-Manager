import subprocess
import os
import sys

def clear_console():
    """Clear the console screen for better UI."""
    os.system('cls' if os.name == 'nt' else 'clear')

def execute_adb_command(command):
    """Execute an ADB command and return the output."""
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            print(f"\nError: {result.stderr.strip()}\n")
            return None
    except Exception as e:
        print(f"\nAn error occurred: {e}\n")
        return None

def check_device():
    """Check if any device is connected and return its name."""
    print("\nChecking for connected devices...")
    command = "adb devices"
    output = execute_adb_command(command)
    if output:
        lines = output.splitlines()
        devices = [line.split()[0] for line in lines if "device" in line and not line.startswith("List of devices")]
        if devices:
            # Retrieve the first device's name (assuming only one is connected)
            device_name_command = f"adb -s {devices[0]} shell getprop ro.product.model"
            device_name = execute_adb_command(device_name_command) or "Unknown Device"
            print(f"\nConnected device: {device_name}")
            return device_name
    print("\nNo devices detected. Please connect a device and ensure USB debugging is enabled.")
    return None

def list_packages():
    """List all packages installed on the connected device."""
    print("\nFetching package list...\n")
    command = "adb shell pm list packages"
    output = execute_adb_command(command)
    if output:
        packages = [line.replace("package:", "") for line in output.splitlines()]
        for package in packages:
            print(package)
        return packages
    else:
        print("\nFailed to retrieve package list. Ensure ADB is set up correctly.")
        return []

def search_package(packages):
    """Search for a package name and provide additional options."""
    search_term = input("\nEnter the package name to search for: ").strip()
    matching_packages = [pkg for pkg in packages if search_term in pkg]
    
    if matching_packages:
        print("\nMatching packages found:\n")
        for i, pkg in enumerate(matching_packages, start=1):
            print(f"{i}. {pkg}")
        
        # Prompt user to choose a package for additional options
        while True:
            try:
                choice = int(input("\nEnter the number of the package to interact with (or 0 to return to the main menu): "))
                if choice == 0:
                    return
                elif 1 <= choice <= len(matching_packages):
                    selected_package = matching_packages[choice - 1]
                    package_actions(selected_package)
                    return
                else:
                    print("\nInvalid choice. Please select a valid option.")
            except ValueError:
                print("\nInvalid input. Please enter a number.")
    else:
        print("\nNo matching packages found.")

def package_actions(package_name):
    """Perform actions on a selected package."""
    while True:
        print(f"\nPackage: {package_name}")
        print("1. Open the app")
        print("2. Uninstall the app")
        print("3. Return to the main menu")
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            print(f"\nAttempting to open {package_name}...")
            command = f"adb shell monkey -p {package_name} -c android.intent.category.LAUNCHER 1"
            output = execute_adb_command(command)
            if output:
                print(f"\nOpened {package_name} successfully.")
            else:
                print(f"\nFailed to open {package_name}.")
        elif choice == "2":
            uninstall_package(package_name)
            return  # Return to the main menu after uninstalling
        elif choice == "3":
            return
        else:
            print("\nInvalid choice. Please try again.")

def uninstall_package(package_name=None):
    """Uninstall a package."""
    if not package_name:
        package_name = input("\nEnter the full package name to uninstall: ").strip()
    print(f"\nAttempting to uninstall {package_name}...\n")
    command = f"adb uninstall {package_name}"
    output = execute_adb_command(command)
    if output and "Success" in output:
        print(f"\nPackage {package_name} uninstalled successfully.")
    else:
        print(f"\nFailed to uninstall package {package_name}. Please check the package name.")

def about():
    """Display information about the developer and software."""
    clear_console()
    print("=" * 50)
    print(" " * 14 + "About ADB Package Manager")
    print("=" * 50)
    print("\nThis software is an ADB Package Manager that allows you to:")
    print("- List all installed apps on your Android device.")
    print("- Search for specific packages.")
    print("- Uninstall user and system apps.")
    print("- Launch apps directly from the terminal.")
    print("\nDeveloped by: [Your Name]")
    print("Version: 1.0")
    print("GitHub: https://github.com/your-profile (replace with your link)")
    print("\nNote: Ensure ADB is properly configured and your device has USB debugging enabled.")
    print("=" * 50)
    input("\nPress Enter to return to the main menu...")

def main():
    """Main menu-driven program."""
    device_name = check_device()
    if not device_name:
        input("\nPress Enter to exit...")
        sys.exit(1)

    packages = []
    while True:
        clear_console()
        print("=" * 50)
        print(f"ADB Package Manager | Connected Device: {device_name}")
        print("=" * 50)
        print("\n1. List all packages")
        print("2. Search for a package")
        print("3. Uninstall a package")
        print("4. Uninstall a system app (user 0)")
        print("5. About")
        print("6. Exit")
        print("\n" + "=" * 50)
        
        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            clear_console()
            packages = list_packages()
            input("\nPress Enter to return to the main menu...")
        elif choice == "2":
            if not packages:
                packages = list_packages()
            clear_console()
            search_package(packages)
        elif choice == "3":
            clear_console()
            uninstall_package()
            input("\nPress Enter to return to the main menu...")
        elif choice == "4":
            clear_console()
            uninstall_package(use_system_user=True)
            input("\nPress Enter to return to the main menu...")
        elif choice == "5":
            about()
        elif choice == "6":
            clear_console()
            print("\nExiting... Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again.")
            input("\nPress Enter to return to the main menu...")

if __name__ == "__main__":
    main()
