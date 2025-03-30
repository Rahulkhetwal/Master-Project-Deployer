@echo off

:: Check if Poetry is installed
where poetry >nul 2>nul
IF %ERRORLEVEL% NEQ 0 (
    echo Poetry is not installed. Please install Poetry first.
    exit /b
)

:: Create virtual environment and install dependencies
echo Setting up virtual environment...
poetry install

echo Environment setup complete!
