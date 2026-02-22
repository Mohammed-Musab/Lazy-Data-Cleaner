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

:: Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo Python not found. Downloading Python %PYTHON_VERSION%...
    echo.
    
    curl -L "%PYTHON_URL%" -o "%PYTHON_INSTALLER%"
    if errorlevel 1 (
        echo ERROR: Failed to download Python.
        pause
        exit /b 1
    )
    
    echo Installing Python %PYTHON_VERSION%...
    "%PYTHON_INSTALLER%" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    
    echo Cleaning up installer...
    del "%PYTHON_INSTALLER%"
    
    echo.
    echo Refreshing environment...
    timeout /t 3 >nul
) else (
    echo Python already installed.
)

echo.
echo Verifying Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python is still not available.
    echo Please restart your computer and run setup.bat again.
    pause
    exit /b 1
)

echo.
echo Upgrading pip...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo ERROR: Failed to upgrade pip.
    pause
    exit /b 1
)

echo.
echo Installing required Python packages...
echo Installing: colorama, pandas, numpy
python -m pip install colorama pandas numpy
if errorlevel 1 (
    echo ERROR: Failed to install required packages.
    echo Please check your internet connection and try again.
    pause
    exit /b 1
)

echo.
echo ======================================
echo   Setup completed successfully!
echo   You can now run run.bat
echo ======================================
pause
