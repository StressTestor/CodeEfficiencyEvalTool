@echo off
:: Launch the Python script to measure code generation efficiency

set SCRIPT_DIR=%~dp0
set PYTHON_SCRIPT=%SCRIPT_DIR%code_efficiency.py

:: Check if python is installed in system PATH
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in the system PATH.
    pause
    exit /b 1
)

if not exist "%PYTHON_SCRIPT%" (
    echo Failed to find the script: %PYTHON_SCRIPT%
    pause
    exit /b 1
)

start cmd /k python "%PYTHON_SCRIPT%"
