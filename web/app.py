"""
Simple web application for testing liturgical calendar calculations.

This application allows liturgical experts to validate date calculations
by entering a year and viewing all calculated liturgical dates.
"""

import sys
sys.path.insert(0, '../src')

from flask import Flask, render_template, request
from calendario_liturgico import LiturgicalCalendar

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Main page with year input and results."""
    result = None
    error = None
    year = None

    if request.method == 'POST':
        try:
            year = int(request.form.get('year', ''))
            cal = LiturgicalCalendar(year)
            result = cal.get_all_dates()
        except ValueError as e:
            error = str(e)
        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template('index.html', result=result, error=error, year=year)


if __name__ == '__main__':
    print("=" * 60)
    print("Liturgical Calendar - Web Interface")
    print("=" * 60)
    print("\nStarting web server...")
    print("Open your browser at: http://localhost:5000")
    print("\nPress CTRL+C to stop the server")
    print("=" * 60)
    app.run(debug=True, host='0.0.1.2', port=5000)
