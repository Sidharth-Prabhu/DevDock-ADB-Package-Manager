@echo off

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Python is not installed. Opening Python website...
    start https://www.python.org/downloads/
    exit /b
)

echo Python is installed.

REM Check if ADB is installed
adb --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo ADB is not installed. Downloading ADB...
    powershell -Command "Invoke-WebRequest -Uri https://dl.google.com/android/repository/platform-tools-latest-windows.zip -OutFile platform-tools.zip"
    if %ERRORLEVEL% neq 0 (
        echo Failed to download ADB. Exiting...
        exit /b
    )
    echo Extracting ADB...
    powershell -Command "Expand-Archive -Path platform-tools.zip -DestinationPath .\platform-tools"
    if %ERRORLEVEL% neq 0 (
        echo Failed to extract ADB. Exiting...
        exit /b
    )
    echo Adding ADB to PATH...
    setx PATH "%cd%\platform-tools;%%PATH%%" >nul
    if %ERRORLEVEL% neq 0 (
        echo Failed to add ADB to PATH. Exiting...
        exit /b
    )
    echo ADB installed and added to PATH.
)

echo ADB is installed.

REM Reload the PATH
echo Reloading PATH...
powershell -Command "$env:Path = [System.Environment]::GetEnvironmentVariable('Path', 'Machine')"

echo PATH reloaded.

REM Check if virtual environment exists
if not exist "venv" (
    echo Virtual environment not found. Creating...
    python -m venv venv
    if %ERRORLEVEL% neq 0 (
        echo Failed to create virtual environment. Exiting...
        exit /b
    )
)

echo Virtual environment exists.

REM Activate the virtual environment
call "venv\Scripts\activate.bat"
if %ERRORLEVEL% neq 0 (
    echo Failed to activate virtual environment. Exiting...
    exit /b
)

echo Virtual environment activated.

REM Install the required package
pip install qrcode
if %ERRORLEVEL% neq 0 (
    echo Failed to install 'qrcode' package. Exiting...
        exit /b
)

echo 'qrcode' package installed.

REM Run the Python script
python devdock.py
if %ERRORLEVEL% neq 0 (
    echo Failed to run the Python script. Exiting...
    exit /b
)

echo Python script executed successfully.
exit /b
