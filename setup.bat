@echo off
setlocal enabledelayedexpansion

echo =============================================
echo Lazy Data Cleaner - Full Setup (Python + Libraries)
echo =============================================
echo.

:: Define Python version and paths
set PY_VERSION=3.11.9
set PY_URL=https://www.python.org/ftp/python/%PY_VERSION%/python-%PY_VERSION%-amd64.exe
set PY_INSTALLER=%TEMP%\python-%PY_VERSION%-amd64.exe
:: Default user install location
set PY_USER_DIR=%LOCALAPPDATA%\Programs\Python\Python311

:: Check if Python 3.11.9 is already in PATH
python --version 2>&1 | find "%PY_VERSION%" >nul
if %errorlevel% equ 0 (
    echo Python %PY_VERSION% is already installed and in PATH.
    goto install_packages
)

:: Also check the typical user install location
if exist "%PY_USER_DIR%\python.exe" (
    echo Found Python %PY_VERSION% in %PY_USER_DIR%
    set "PATH=%PY_USER_DIR%;%PY_USER_DIR%\Scripts;%PATH%"
    goto install_packages
)

echo Python %PY_VERSION% not found. Downloading installer...
powershell -Command "Invoke-WebRequest -Uri '%PY_URL%' -OutFile '%PY_INSTALLER%'"
if %errorlevel% neq 0 (
    echo Failed to download Python installer. Check your internet connection.
    pause
    exit /b 1
)

echo Installing Python %PY_VERSION% for current user (silent)...
start /wait %PY_INSTALLER% /quiet InstallAllUsers=0 PrependPath=1 Include_test=0
if %errorlevel% neq 0 (
    echo Installation failed. You may need to run this script as Administrator.
    pause
    exit /b 1
)

:: After installation, add the install dir to PATH for this session
set "PATH=%PY_USER_DIR%;%PY_USER_DIR%\Scripts;%PATH%"
echo Python %PY_VERSION% installed successfully.

:install_packages
echo.
echo Installing required Python packages...

:: Use pip from the user install location (or system if already there)
"%PY_USER_DIR%\Scripts\pip.exe" --version >nul 2>&1
if %errorlevel% neq 0 (
    :: Fallback to pip in PATH
    pip --version >nul 2>&1
    if !errorlevel! neq 0 (
        echo ERROR: pip not found. Python may not be installed correctly.
        pause
        exit /b 1
    ) else (
        set PIP_CMD=pip
    )
) else (
    set PIP_CMD="%PY_USER_DIR%\Scripts\pip.exe"
)

echo Using: !PIP_CMD!
!PIP_CMD! install --upgrade pip
!PIP_CMD! install colorama pandas

if %errorlevel% neq 0 (
    echo.
    echo Package installation failed. You can try manually:
    echo   pip install colorama pandas
) else (
    echo.
    echo All libraries installed successfully!
)

echo.
echo =============================================
echo Setup complete! You can now run Lazy Data Cleaner.
echo =============================================
pause