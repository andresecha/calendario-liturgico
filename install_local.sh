#!/bin/bash
# Local installation script for calendario-liturgico

echo "================================"
echo "Liturgical Calendar - Local Setup"
echo "================================"
echo

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    exit 1
fi

echo "1. Installing package in development mode..."
python3 -m pip install -e .

echo
echo "2. Installing development dependencies..."
python3 -m pip install -e ".[dev]"

echo
echo "3. Installing web dependencies (optional)..."
python3 -m pip install -e ".[web]"

echo
echo "================================"
echo "Installation complete!"
echo "================================"
echo
echo "To test the installation:"
echo "  python3 -c 'from calendario_liturgico import LiturgicalCalendar; print(LiturgicalCalendar(2024).get_easter_sunday())'"
echo
echo "To run tests:"
echo "  pytest"
echo
echo "To start web interface:"
echo "  python3 web/app.py"
