# =============================================================================
# CALENDARIO LITÚRGICO - Módulo de Calculadores
# =============================================================================
# 
# PROPÓSITO:
# Contiene algoritmos para calcular fechas litúrgicas que no están
# pre-calculadas, específicamente la Pascua gregoriana.
# 
# FUNCIONALIDAD PRINCIPAL:
# - Implementa el algoritmo de Computus para calcular la Pascua gregoriana
# - Valida que el año sea válido para el calendario gregoriano (>= 1583)
# 
# USO EN EL ENTORNO:
# Este módulo es usado por core.py cuando se necesita calcular la Pascua
# para años del calendario gregoriano (1583 en adelante).
# 
# ALGORITMO IMPLEMENTADO:
# El algoritmo de Computus es un método matemático desarrollado por la Iglesia
# para determinar la fecha de Pascua basándose en el ciclo lunar y el equinoccio
# de primavera.
#
# =============================================================================

"""Calculators for liturgical dates."""

import datetime
from typing import Optional


def calculate_gregorian_easter(year: int) -> datetime.date:
    """
    Calcula la fecha de Pascua usando el algoritmo de Computus gregoriano.
    
    El algoritmo de Computus es un método matemático que calcula la fecha
    de Pascua basándose en el ciclo lunar (metónico) y las reglas establecidas
    por el Concilio de Nicea (325 d.C.) y reformadas por el Papa Gregorio XIII
    en 1582.
    
    Regla de Pascua: Pascua es el primer domingo después de la primera luna llena
    que ocurre en o después del equinoccio de primavera (21 de marzo).

    Parameters
    ----------
    year : int
        El año para calcular la Pascua (debe ser >= 1583).

    Returns
    -------
    datetime.date
        La fecha del Domingo de Pascua.

    Raises
    ------
    ValueError
        Si el año es menor que 1583 (antes de la reforma gregoriana).

    Notes
    -----
    Utiliza el algoritmo de Computus para el calendario gregoriano.
    Este algoritmo calcula la fecha de Pascua basándose en el ciclo lunar
    y las reglas establecidas por el Concilio de Nicea.
    
    El algoritmo usa varios cálculos modulares para:
    - a: Posición del año en el ciclo metónico (19 años)
    - b,c: Siglo y posición en el siglo
    - d: Corrección de años bisiestos
    - e: Día de la semana del equinoccio
    - f: Día del mes resultante

    References
    ----------
    .. [1] Meeus, Jean (1991). "Astronomical Algorithms"
    .. [2] Gauss, Carl Friedrich. "Berechnung des Osterfestes" (1800)

    Examples
    --------
    >>> calculate_gregorian_easter(2024)
    datetime.date(2024, 3, 31)
    >>> calculate_gregorian_easter(2025)
    datetime.date(2025, 4, 20)
    """
    # Validar que el año sea válido para calendario gregoriano
    if year < 1583:
        raise ValueError("Year must be >= 1583 for Gregorian calendar")

    # Aplicar el algoritmo de Computus
    # Paso 1: Calcular el número dorado (posición en el ciclo metónico de 19 años)
    a = year % 19
    
    # Paso 2: Calcular el siglo y la posición dentro del siglo
    b = year // 100
    c = year % 100
    
    # Paso 3: Calcular correcciones para luna llena pascual
    # Esta fórmula compleja ajusta por los años bisiestos y el ciclo solar
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    
    # Paso 4: Calcular el día de la semana
    # e determina cuántos días después de la luna llena cae el domingo
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    
    # Paso 5: Calcular la fecha resultante
    # f combina d y e para obtener el día del mes
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    
    # Paso 6: Extraer mes y día
    month = f // 31
    day = f % 31 + 1
    
    return datetime.date(year, month, day)
