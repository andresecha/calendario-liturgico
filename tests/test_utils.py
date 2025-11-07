"""Tests for utils module."""

import pytest

from calendario_liturgico import is_leap_year


class TestUtils:
    """Tests for utility functions."""

    def test_gregorian_leap_years(self) -> None:
        """Test Gregorian leap years."""
        assert is_leap_year(2024) is True
        assert is_leap_year(2023) is False
        assert is_leap_year(2000) is True
        assert is_leap_year(1900) is False

    def test_julian_leap_years(self) -> None:
        """Test Julian leap years."""
        assert is_leap_year(1200, is_julian=True) is True
        assert is_leap_year(1201, is_julian=True) is False
        assert is_leap_year(1900, is_julian=True) is True
