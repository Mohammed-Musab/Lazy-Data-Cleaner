@echo off
title Lazy Data Cleaner - Full Setup
setlocal

echo ======================================
echo   Lazy Data Cleaner - Full Setup
echo ======================================
echo.

:: -----------------------------
:: SETTINGS
:: -----------------------------
set PYTHON_VERSION=3.11.9
set PYTHON_INSTALLER=python-3.11.9-amd64.exe
set PYTHON_URL=https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe

:: -----------------------------
:: CHECK PYTHON
:: -----------------------------
python --version >nul 2>&1
if errorlevel 1 (
    echo Python not found.
    echo Downloading Python %PYTHON_VERSION%...
    echo.

    :: Download Python installer
    curl -L "%PYTHON_URL%" -o "%PYTHON_INSTALLER%"
    if errorlevel 1 (
        echo ERROR: Failed to download Python.
        pause
        exit /b
    )

    echo Installing Python %PYTHON_VERSION%...
    echo.

    :: Silent install Python (for all users, add to PATH)
    "%PYTHON_INSTALLER%" ^
        /quiet ^
        InstallAllUsers=1 ^
        PrependPath=1 ^
        Include_test=0

    echo Python installation finished.
    echo.

    :: Cleanup installer
    del "%PYTHON_INSTALLER%"
) else (
    echo Python already installed.
)

echo.
echo Refreshing environment...
timeout /t 3 >nul

:: -----------------------------
:: VERIFY PYTHON
:: -----------------------------
python --version
if errorlevel 1 (
    echo ERROR: Python is still not available.
    echo Please restart your computer and run setup.bat again.
    pause
    exit /b
)

echo.
echo Upgrading pip...
python -m pip install --upgrade pip

echo.
echo Installing required Python packages...
python -m pip install colorama numpy pandas

echo.
echo ======================================
echo   Setup completed successfully!
echo   You can now run run.bat
echo ======================================
pause
