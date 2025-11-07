# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1] - 2025-11-06

### Changed - BREAKING CHANGES
- **All API in English**: All function and method names changed to English
  - `obtener_*` → `get_*`
  - `es_año_bisiesto` → `is_leap_year`
  - `calcular_pascua_gregoriano` → `calculate_gregorian_easter`
  - `CalendarioLiturgico` → `LiturgicalCalendar`
- **Module names in English**: 
  - `utilidades.py` → `utils.py`
  - `calculadores.py` → `calculators.py`
  - `datos.py` → `data.py`
- **License changed to MIT**: Now free for commercial use

### Added
- Web interface for testing with experts (`web/app.py`)
- Local installation script (`install_local.sh`)
- Bilingual README (English/Spanish)
- No special characters in code (no ñ, no accents)

### Removed
- All Spanish function names
- References to specific research projects
- CC-BY-NC-SA license (replaced with MIT)

## [0.0.0] - 2025-11-06

### Added
- Initial implementation of `CalendarioLiturgico`
- Support for Julian calendar (years 532-1582)
- Support for Gregorian calendar (years 1583+)
- Calculation of all major liturgical dates
- Complete Julian Easter dates dictionary (years 532-1583)
- Computus algorithm for Gregorian Easter
- Complete NumPy-style documentation
- Unit tests with pytest
- Full type hints for Python 3.8+

---

[0.2.0]: https://github.com/andresecha/libraryProject/compare/v0.1.0...v0.2.0
[0.0.0]: https://github.com/andresecha/libraryProject/releases/tag/v0.1.0
