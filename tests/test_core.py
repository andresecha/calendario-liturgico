"""Tests for the core module."""

import datetime
import pytest

from calendario_liturgico import LiturgicalCalendar


class TestLiturgicalCalendar:
    """Tests for Liturgical Calendar class."""

    def test_create_gregorian_calendar(self) -> None:
        """Test creation of Gregorian calendar."""
        cal = LiturgicalCalendar(2024)
        assert cal.year == 2024
        assert not cal.is_julian
        assert isinstance(cal.easter_date, datetime.date)

    def test_create_julian_calendar(self) -> None:
        """Test creation of Julian calendar."""
        cal = LiturgicalCalendar(1200)
        assert cal.year == 1200
        assert cal.is_julian
        assert isinstance(cal.easter_date, datetime.date)

    def test_easter_2024(self) -> None:
        """Test Easter date for 2024."""
        cal = LiturgicalCalendar(2024)
        assert cal.get_easter_sunday() == datetime.date(2024, 3, 31)

    def test_ash_wednesday_2024(self) -> None:
        """Test Ash Wednesday 2024."""
        cal = LiturgicalCalendar(2024)
        assert cal.get_ash_wednesday() == datetime.date(2024, 2, 14)

    def test_pentecost_2024(self) -> None:
        """Test Pentecost 2024."""
        cal = LiturgicalCalendar(2024)
        assert cal.get_pentecost() == datetime.date(2024, 5, 19)

    def test_palm_sunday(self) -> None:
        """Test Palm Sunday."""
        cal = LiturgicalCalendar(2024)
        assert cal.get_palm_sunday() == datetime.date(2024, 3, 24)

    def test_good_friday(self) -> None:
        """Test Good Friday."""
        cal = LiturgicalCalendar(2024)
        assert cal.get_good_friday() == datetime.date(2024, 3, 29)

    def test_julian_year_no_data(self) -> None:
        """Test error when no data for Julian year."""
        with pytest.raises(ValueError, match="No Easter data"):
            LiturgicalCalendar(400)

    def test_get_all_dates(self) -> None:
        """Test getting all dates."""
        cal = LiturgicalCalendar(2024)
        dates = cal.get_all_dates()
        assert isinstance(dates, dict)
        assert dates["Year"] == 2024
        assert dates["Calendar"] == "Gregorian"
