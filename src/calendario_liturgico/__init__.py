# =============================================================================
# CALENDARIO LITÚRGICO - Archivo de Inicialización del Paquete
# =============================================================================
# 
# PROPÓSITO:
# Este archivo define el punto de entrada principal del paquete calendario_liturgico.
# Exporta las clases y funciones principales que los usuarios necesitarán.
# 
# FUNCIONALIDAD:
# - Define la versión del paquete (__version__)
# - Exporta la clase principal LiturgicalCalendar
# - Exporta funciones auxiliares (is_leap_year, calculate_gregorian_easter)
# - Exporta datos (JULIAN_EASTER_DATES)
# - Proporciona metadatos del paquete (autor, licencia)
# 
# USO EN EL ENTORNO:
# Cuando un usuario hace "from calendario_liturgico import LiturgicalCalendar",
# Python busca este archivo primero y carga lo que está en __all__
#
# =============================================================================

"""
Liturgical Calendar
===================

A Python library for calculating Christian liturgical dates
in both Julian and Gregorian calendars.

This library is especially useful for historians working
with documents that use liturgical dates instead of civil dates.

Basic Usage
-----------
>>> from calendario_liturgico import LiturgicalCalendar
>>> cal = LiturgicalCalendar(2024)
>>> print(cal.get_easter_sunday())
2024-03-31

Author
------
Andres Felipe Echavarria Pelaez

License
-------
MIT License

Version
-------
0.0.1
"""

# Información del paquete
__version__ = "0.0.1"
__author__ = "Andres Felipe Echavarria Pelaez"
__license__ = "MIT"

# Lista de lo que se exporta cuando se hace "from calendario_liturgico import *"
__all__ = [
    "LiturgicalCalendar",           # Clase principal para cálculos litúrgicos
    "calculate_gregorian_easter",   # Función para calcular Pascua gregoriana
    "is_leap_year",                 # Función para verificar años bisiestos
    "JULIAN_EASTER_DATES",          # Diccionario de fechas de Pascua juliana
]

# Importaciones desde los módulos internos
from .core import LiturgicalCalendar
from .calculators import calculate_gregorian_easter
from .utils import is_leap_year
from .data import JULIAN_EASTER_DATES
