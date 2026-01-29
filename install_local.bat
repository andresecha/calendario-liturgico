
REM Local installation script for calendario-liturgico (Windows)

echo ================================
echo Liturgical Calendar - Local Setup
echo ================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python 3 is not installed
    echo Please download Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

echo 1. Installing package in development mode...
python -m pip install -e .

echo.
echo 2. Installing development dependencies...
python -m pip install -e .[dev]

echo.
echo 3. Installing web dependencies (optional)...
python -m pip install -e .[web]

echo.
echo ================================
echo Installation complete!
echo ================================
echo.
echo To test the installation:
echo   python -c "from calendario_liturgico import LiturgicalCalendar; print(LiturgicalCalendar(2024).get_easter_sunday())"
echo.
echo To run tests:
echo   pytest
echo.
echo To start web interface:
echo   cd web
echo   python app.py
echo.
pause
