@echo off
setlocal enabledelayedexpansion

echo =============================================
echo Lazy Data Cleaner - Full Setup (Python + Virtual Environment)
echo =============================================
echo.

:: Define Python version and paths
set PY_VERSION=3.11.9
set PY_URL=https://www.python.org/ftp/python/%PY_VERSION%/python-%PY_VERSION%-amd64.exe
set PY_INSTALLER=%TEMP%\python-%PY_VERSION%-amd64.exe
:: Default user install location
set PY_USER_DIR=%LOCALAPPDATA%\Programs\Python\Python311

:: Get the directory where this script is located
set "SCRIPT_DIR=%~dp0"
set "VENV_DIR=%SCRIPT_DIR%venv"

:: Check if Python 3.11.9 is already in PATH
python --version 2>&1 | find "%PY_VERSION%" >nul
if %errorlevel% equ 0 (
    echo Python %PY_VERSION% is already installed and in PATH.
    goto create_venv
)

:: Also check the typical user install location
if exist "%PY_USER_DIR%\python.exe" (
    echo Found Python %PY_VERSION% in %PY_USER_DIR%
    set "PATH=%PY_USER_DIR%;%PY_USER_DIR%\Scripts;%PATH%"
    goto create_venv
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

:create_venv
echo.
echo Setting up virtual environment...

:: Use the Python we just installed (or found) to create a venv
if exist "%VENV_DIR%" (
    echo Virtual environment already exists at %VENV_DIR%
) else (
    echo Creating virtual environment in %VENV_DIR%...
    python -m venv "%VENV_DIR%"
    if !errorlevel! neq 0 (
        echo Failed to create virtual environment.
        pause
        exit /b 1
    )
    echo Virtual environment created.
)

:: Define paths to venv's Python and pip
set "VENV_PYTHON=%VENV_DIR%\Scripts\python.exe"
set "VENV_PIP=%VENV_DIR%\Scripts\pip.exe"

:: Upgrade pip in the venv
echo Upgrading pip in virtual environment...
"%VENV_PYTHON%" -m pip install --upgrade pip

:: Install required packages
echo Installing colorama and pandas into virtual environment...
"%VENV_PIP%" install colorama pandas

if %errorlevel% neq 0 (
    echo.
    echo Package installation failed. You can try manually:
    echo   "%VENV_PIP%" install colorama pandas
) else (
    echo.
    echo All libraries installed successfully into the virtual environment!
)

echo.
echo =============================================
echo Setup complete!
echo =============================================
echo.
echo To run Lazy Data Cleaner using this environment:
echo   1. Activate the environment:
echo        "%VENV_DIR%\Scripts\activate.bat"
echo   2. Then run:
echo        python main.py
echo.
echo Or use the helper script below (save as run.bat):
echo ------------------------------------------------
echo @echo off
echo call "%VENV_DIR%\Scripts\activate.bat"
echo python main.py
echo pause
echo ------------------------------------------------
pause
