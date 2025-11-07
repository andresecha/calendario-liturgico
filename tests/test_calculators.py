"""Tests for calculators module."""

import datetime
import pytest

from calendario_liturgico import calculate_gregorian_easter


class TestCalculators:
    """Tests for calculator functions."""

    def test_calculate_easter(self) -> None:
        """Test Easter calculation."""
        assert calculate_gregorian_easter(2024) == datetime.date(2024, 3, 31)
        assert calculate_gregorian_easter(2025) == datetime.date(2025, 4, 20)

    def test_invalid_year(self) -> None:
        """Test error for invalid year."""
        with pytest.raises(ValueError, match="must be >= 1583"):
            calculate_gregorian_easter(1582)
