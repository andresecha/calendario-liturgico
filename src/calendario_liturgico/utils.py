# =============================================================================
# CALENDARIO LITÚRGICO - Módulo de Utilidades
# =============================================================================
# 
# PROPÓSITO:
# Proporciona funciones auxiliares que son útiles para cálculos de calendario
# pero que no son específicas de una fecha litúrgica en particular.
# 
# FUNCIONALIDAD PRINCIPAL:
# - Determinar si un año es bisiesto (tanto juliano como gregoriano)
# 
# USO EN EL ENTORNO:
# Este módulo es usado por core.py para proporcionar información adicional
# sobre el año (como si es bisiesto). Las funciones aquí son genéricas
# y podrían usarse en otros contextos de cálculo de calendarios.
#
# =============================================================================

"""Utility functions for calendar calculations."""

from typing import Union


def is_leap_year(year: int, is_julian: bool = False) -> bool:
    """
    Determina si un año es bisiesto según las reglas del calendario especificado.
    
    Los años bisiestos tienen 366 días en lugar de 365, con un día extra (29 de febrero).
    Las reglas para determinar años bisiestos son diferentes entre los calendarios
    juliano y gregoriano.
    
    REGLAS DEL CALENDARIO JULIANO:
    - Un año es bisiesto si es divisible por 4
    - No hay excepciones
    - Esto resulta en un año promedio de 365.25 días
    
    REGLAS DEL CALENDARIO GREGORIANO:
    - Un año es bisiesto si es divisible por 4
    - EXCEPTO si es divisible por 100 (entonces NO es bisiesto)
    - EXCEPTO si es divisible por 400 (entonces SÍ es bisiesto)
    - Esto resulta en un año promedio de 365.2425 días (más preciso)
    
    Ejemplos de casos especiales:
    - 1900: No bisiesto (gregoriano) - divisible por 100 pero no por 400
    - 1900: Sí bisiesto (juliano) - divisible por 4
    - 2000: Sí bisiesto (gregoriano) - divisible por 400
    - 2024: Sí bisiesto (ambos) - divisible por 4, no por 100

    Parameters
    ----------
    year : int
        El año a verificar.
    is_julian : bool, optional
        Si True, usa reglas del calendario juliano.
        Si False, usa reglas del calendario gregoriano.
        Por defecto False (usa gregoriano).

    Returns
    -------
    bool
        True si el año es bisiesto, False en caso contrario.

    Examples
    --------
    >>> is_leap_year(2024)
    True
    >>> is_leap_year(1900)
    False
    >>> is_leap_year(1900, is_julian=True)
    True

    Notes
    -----
    En el calendario juliano, un año es bisiesto si es divisible por 4.
    En el calendario gregoriano, un año es bisiesto si es divisible por 4,
    excepto los años divisibles por 100, a menos que también sean divisibles por 400.
    
    El calendario gregoriano fue introducido por el Papa Gregorio XIII en 1582
    para corregir el desfase del calendario juliano con respecto al año solar real.
    """
    if is_julian:
        # Regla simple del calendario juliano: divisible por 4
        return year % 4 == 0
    else:
        # Regla compleja del calendario gregoriano:
        # 1. Divisible por 4: candidato a bisiesto
        # 2. Si es divisible por 100: NO es bisiesto (excepción)
        # 3. Si es divisible por 400: SÍ es bisiesto (excepción de la excepción)
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
