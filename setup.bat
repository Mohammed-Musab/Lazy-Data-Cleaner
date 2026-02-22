@echo off
title Lazy Data Cleaner - Full Setup
setlocal enabledelayedexpansion

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
set INSTALLED=0

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
    
    set INSTALLED=1
) else (
    echo Python already installed.
)

:: If we just installed Python, add its directory to the current PATH
if %INSTALLED%==1 (
    echo.
    echo Refreshing environment...
    :: Determine Python installation directory (default for all users, 64-bit)
    for /f "tokens=1,2 delims=." %%a in ("%PYTHON_VERSION%") do (
        set PY_MAJOR=%%a
        set PY_MINOR=%%b
    )
    set "PY_DIR_NAME=Python!PY_MAJOR!!PY_MINOR!"
    set "PYTHON_DIR=%ProgramFiles%\!PY_DIR_NAME!"
    
    :: Check if python.exe exists at the default location
    if exist "!PYTHON_DIR!\python.exe" (
        set "PATH=%PATH%;!PYTHON_DIR!"
    ) else (
        echo Warning: Could not find Python installation at expected location: !PYTHON_DIR!
        echo Attempting to locate Python...
        :: Try common locations
        set "FOUND="
        if exist "%ProgramFiles%\Python*" (
            for /d %%d in ("%ProgramFiles%\Python*") do (
                if exist "%%d\python.exe" (
                    set "PYTHON_DIR=%%d"
                    set "PATH=%PATH%;%%d"
                    set FOUND=1
                )
            )
        )
        if not defined FOUND (
            if exist "%LocalAppData%\Programs\Python\Python*" (
                for /d %%d in ("%LocalAppData%\Programs\Python\Python*") do (
                    if exist "%%d\python.exe" (
                        set "PYTHON_DIR=%%d"
                        set "PATH=%PATH%;%%d"
                        set FOUND=1
                    )
                )
            )
        )
        if not defined FOUND (
            echo ERROR: Could not locate Python installation. Please add it manually to PATH.
            pause
            exit /b 1
        )
    )
    timeout /t 3 >nul
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
