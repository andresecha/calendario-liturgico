# =============================================================================
# CALENDARIO LITÚRGICO - Módulo Principal (Core)
# =============================================================================
# 
# PROPÓSITO:
# Define la clase LiturgicalCalendar que es el corazón de la librería.
# Esta clase permite calcular todas las fechas litúrgicas cristianas importantes
# tanto para el calendario juliano como el gregoriano.
# 
# FUNCIONALIDAD PRINCIPAL:
# - Determinar automáticamente si un año usa calendario juliano o gregoriano
# - Calcular la fecha de Pascua (base de muchas otras fechas)
# - Calcular todas las fechas móviles del calendario litúrgico
# - Proporcionar fechas fijas del calendario litúrgico
# 
# USO EN EL ENTORNO:
# Este es el módulo más importante de la librería. Los usuarios crearán
# instancias de LiturgicalCalendar y llamarán sus métodos para obtener fechas.
#
# DEPENDENCIAS:
# - datetime: Para manejar fechas
# - typing: Para type hints
# - .data: Para fechas de Pascua juliana pre-calculadas
# - .calculators: Para calcular Pascua gregoriana
# - .utils: Para funciones auxiliares
#
# =============================================================================

"""Main class for liturgical calendar."""

import datetime
from typing import Dict, List, Tuple, Any, Union

# Importaciones desde otros módulos de la librería
from .data import JULIAN_EASTER_DATES
from .calculators import calculate_gregorian_easter
from .utils import is_leap_year


class LiturgicalCalendar:
    """
    Representa un calendario litúrgico para un año dado.
    
    Esta clase permite calcular las fechas de las principales
    celebraciones litúrgicas cristianas tanto para el calendario
    juliano como gregoriano.

    Parameters
    ----------
    year : int
        El año del calendario litúrgico.

    Attributes
    ----------
    year : int
        El año del calendario.
    is_julian : bool
        True si usa calendario juliano, False si gregoriano.
    easter_date : datetime.date
        La fecha de Domingo de Pascua.

    Raises
    ------
    ValueError
        Si no hay datos de Pascua para el año juliano especificado.

    Examples
    --------
    >>> cal = LiturgicalCalendar(2024)
    >>> cal.get_easter_sunday()
    datetime.date(2024, 3, 31)

    >>> cal_julian = LiturgicalCalendar(1200)
    >>> cal_julian.is_julian
    True

    Notes
    -----
    El calendario juliano se usa para años hasta 1582 (inclusive),
    y el gregoriano para años 1583 en adelante. La transición corresponde
    a la reforma del calendario por el Papa Gregorio XIII en 1582.
    """

    def __init__(self, year: int):
        """
        Inicializa el calendario litúrgico para un año específico.
        
        Determina automáticamente si el año usa calendario juliano o gregoriano
        y calcula la fecha de Pascua correspondiente.
        """
        # Almacenar el año
        self.year = year
        
        # Determinar tipo de calendario: juliano si año <= 1582, gregoriano si > 1582
        self.is_julian = year <= 1582

        if self.is_julian:
            # Para calendario juliano, buscar fecha pre-calculada en el diccionario
            if year not in JULIAN_EASTER_DATES:
                raise ValueError(
                    f"No Easter data available for Julian year {year}."
                )
            # Parsear la fecha del formato "MM-DD"
            month, day = map(int, JULIAN_EASTER_DATES[year].split('-'))
            self.easter_date = datetime.date(year, month, day)
        else:
            # Para calendario gregoriano, usar el algoritmo de Computus
            self.easter_date = calculate_gregorian_easter(year)

    # =========================================================================
    # MÉTODOS PARA TIEMPO DE CUARESMA Y SEMANA SANTA
    # =========================================================================

    def get_ash_wednesday(self) -> datetime.date:
        """
        Calcula la fecha del Miércoles de Ceniza.
        
        El Miércoles de Ceniza marca el inicio de la Cuaresma.
        Se calcula restando 46 días a la Pascua (40 días de Cuaresma
        más 6 domingos que no se cuentan en la Cuaresma).

        Returns
        -------
        datetime.date
            Fecha del Miércoles de Ceniza (46 días antes de Pascua).
        """
        return self.easter_date - datetime.timedelta(days=46)

    def get_palm_sunday(self) -> datetime.date:
        """
        Calcula la fecha del Domingo de Ramos.
        
        El Domingo de Ramos conmemora la entrada triunfal de Jesús en Jerusalén
        y marca el inicio de la Semana Santa.

        Returns
        -------
        datetime.date
            Fecha del Domingo de Ramos (7 días antes de Pascua).
        """
        return self.easter_date - datetime.timedelta(days=7)

    def get_holy_thursday(self) -> datetime.date:
        """
        Calcula la fecha del Jueves Santo.
        
        El Jueves Santo conmemora la Última Cena de Jesús con sus apóstoles
        y el lavatorio de los pies.

        Returns
        -------
        datetime.date
            Fecha del Jueves Santo (3 días antes de Pascua).
        """
        return self.easter_date - datetime.timedelta(days=3)

    def get_good_friday(self) -> datetime.date:
        """
        Calcula la fecha del Viernes Santo.
        
        El Viernes Santo conmemora la crucifixión y muerte de Jesús.
        Es uno de los días más solemnes del calendario litúrgico.

        Returns
        -------
        datetime.date
            Fecha del Viernes Santo (2 días antes de Pascua).
        """
        return self.easter_date - datetime.timedelta(days=2)

    def get_holy_saturday(self) -> datetime.date:
        """
        Calcula la fecha del Sábado Santo.
        
        El Sábado Santo conmemora el día que Jesús pasó en el sepulcro.
        Es un día de espera y preparación para la Vigilia Pascual.

        Returns
        -------
        datetime.date
            Fecha del Sábado Santo (1 día antes de Pascua).
        """
        return self.easter_date - datetime.timedelta(days=1)

    # =========================================================================
    # MÉTODOS PARA TIEMPO PASCUAL
    # =========================================================================

    def get_easter_sunday(self) -> datetime.date:
        """
        Obtiene la fecha del Domingo de Pascua.
        
        La Pascua celebra la resurrección de Jesús y es la festividad
        más importante del calendario litúrgico cristiano. Todas las demás
        fechas móviles se calculan en relación a la Pascua.

        Returns
        -------
        datetime.date
            Fecha del Domingo de Pascua.
        """
        return self.easter_date

    def get_ascension(self) -> datetime.date:
        """
        Calcula la fecha de la Ascensión.
        
        La Ascensión celebra la ascensión de Jesús al cielo.
        Tradicionalmente se calcula 40 días después de Pascua,
        pero se resta un día porque se cuenta el domingo de Pascua.

        Returns
        -------
        datetime.date
            Fecha de la Ascensión (39 días después de Pascua).
        """
        return self.easter_date + datetime.timedelta(days=39)

    def get_pentecost(self) -> datetime.date:
        """
        Calcula la fecha de Pentecostés.
        
        Pentecostés conmemora el descenso del Espíritu Santo sobre
        los apóstoles y marca el final del tiempo pascual.
        Se celebra 50 días después de Pascua (49 días más el día de Pascua).

        Returns
        -------
        datetime.date
            Fecha de Pentecostés (49 días después de Pascua).
        """
        return self.easter_date + datetime.timedelta(days=49)

    def get_trinity_sunday(self) -> datetime.date:
        """
        Calcula la fecha del Domingo de la Trinidad.
        
        El Domingo de la Trinidad celebra la doctrina de la Santísima
        Trinidad y ocurre el domingo siguiente a Pentecostés.

        Returns
        -------
        datetime.date
            Fecha del Domingo de la Trinidad (56 días después de Pascua).
        """
        return self.easter_date + datetime.timedelta(days=56)

    def get_corpus_christi(self) -> datetime.date:
        """
        Calcula la fecha de Corpus Christi (Cuerpo de Cristo).
        
        Corpus Christi celebra la presencia real de Cristo en la Eucaristía.
        Ocurre el jueves después del Domingo de la Trinidad.

        Returns
        -------
        datetime.date
            Fecha de Corpus Christi (60 días después de Pascua).
        """
        return self.easter_date + datetime.timedelta(days=60)

    # =========================================================================
    # MÉTODOS PARA TIEMPO DE ADVIENTO Y NAVIDAD
    # =========================================================================

    def get_advent_start(self) -> datetime.date:
        """
        Calcula la fecha de inicio del Adviento.
        
        El Adviento es el período de preparación para la Navidad.
        Comienza el cuarto domingo antes de Navidad. Para calcularlo:
        1. Tomar la fecha de Navidad (25 de diciembre)
        2. Encontrar el domingo más cercano a Navidad
        3. Retroceder 3 semanas (21 días) para llegar al primer domingo

        Returns
        -------
        datetime.date
            Fecha del primer domingo de Adviento.
        """
        # Navidad es siempre el 25 de diciembre
        christmas = datetime.date(self.year, 12, 25)
        
        # Calcular días hasta el próximo domingo (0=lunes, 6=domingo en weekday())
        days_to_sunday = (7 - christmas.weekday()) % 7
        
        # Retroceder 3 semanas (21 días) desde el cuarto domingo antes de Navidad
        fourth_sunday_before = christmas - datetime.timedelta(
            days=days_to_sunday + 21
        )
        return fourth_sunday_before

    def get_advent_sundays(self) -> List[datetime.date]:
        """
        Calcula las fechas de los cuatro domingos de Adviento.
        
        El Adviento consta de cuatro domingos de preparación antes de Navidad.

        Returns
        -------
        List[datetime.date]
            Lista con las fechas de los cuatro domingos de Adviento.
        """
        advent_start = self.get_advent_start()
        # Crear lista con los 4 domingos (cada 7 días)
        return [advent_start + datetime.timedelta(days=i*7) for i in range(4)]

    # =========================================================================
    # MÉTODOS PARA OTRAS FECHAS LITÚRGICAS IMPORTANTES
    # =========================================================================

    def get_epiphany(self) -> datetime.date:
        """
        Obtiene la fecha de la Epifanía.
        
        La Epifanía celebra la manifestación de Jesús a los Magos de Oriente.
        Es una fecha fija: 6 de enero.

        Returns
        -------
        datetime.date
            Fecha de la Epifanía (6 de enero).
        """
        return datetime.date(self.year, 1, 6)

    def get_baptism_of_the_lord(self) -> datetime.date:
        """
        Calcula la fecha del Bautismo del Señor.
        
        El Bautismo del Señor celebra el bautismo de Jesús por Juan el Bautista.
        Normalmente ocurre el domingo siguiente a la Epifanía.

        Returns
        -------
        datetime.date
            Fecha del Bautismo del Señor (domingo después de Epifanía).
        """
        epiphany = self.get_epiphany()
        # Calcular días hasta el próximo domingo
        days_to_sunday = (7 - epiphany.weekday()) % 7
        # Si Epifanía cae en domingo, Bautismo es el mismo día
        # Si no, es el domingo siguiente
        return epiphany + datetime.timedelta(days=days_to_sunday)

    def get_christ_the_king(self) -> datetime.date:
        """
        Calcula la fecha de Cristo Rey.
        
        La Solemnidad de Cristo Rey se celebra el último domingo antes
        del inicio del Adviento, cerrando el año litúrgico.

        Returns
        -------
        datetime.date
            Fecha de Cristo Rey (último domingo del año litúrgico).
        """
        advent_start = self.get_advent_start()
        # Cristo Rey es el domingo anterior al inicio del Adviento
        return advent_start - datetime.timedelta(days=7)

    # =========================================================================
    # MÉTODOS PARA RANGOS DE TIEMPO LITÚRGICO
    # =========================================================================

    def get_lent_range(self) -> Tuple[datetime.date, datetime.date]:
        """
        Calcula el rango de fechas de la Cuaresma.
        
        La Cuaresma es un período de 40 días (sin contar domingos)
        de preparación para la Pascua. Comienza el Miércoles de Ceniza
        y termina el sábado antes del Domingo de Ramos.

        Returns
        -------
        Tuple[datetime.date, datetime.date]
            Tupla con la fecha de inicio (Miércoles de Ceniza)
            y fecha de fin (sábado antes del Domingo de Ramos).
        """
        start = self.get_ash_wednesday()
        # Termina el día antes del Domingo de Ramos
        end = self.get_palm_sunday() - datetime.timedelta(days=1)
        return start, end

    # =========================================================================
    # MÉTODO PARA OBTENER TODAS LAS FECHAS
    # =========================================================================

    def get_all_dates(self) -> Dict[str, Union[str, datetime.date, List[datetime.date], bool]]:
        """
        Obtiene todas las fechas litúrgicas del año en un diccionario.
        
        Este método es útil para obtener un resumen completo del año litúrgico
        de una sola vez. Incluye información sobre el tipo de calendario,
        si es año bisiesto, y todas las fechas importantes.

        Returns
        -------
        Dict[str, Union[str, datetime.date, List[datetime.date], bool]]
            Diccionario con todas las fechas y metadatos del calendario.
            Las claves incluyen nombres de festividades y metadatos.
        """
        # Obtener los domingos de Adviento
        advent_sundays = self.get_advent_sundays()
        
        # Obtener el rango de Cuaresma
        lent_start, lent_end = self.get_lent_range()
        
        # Construir el diccionario con toda la información
        return {
            # Metadatos del año
            "Year": self.year,
            "Calendar": "Julian" if self.is_julian else "Gregorian",
            "Is Leap Year": is_leap_year(self.year, self.is_julian),
            
            # Tiempo de Navidad y Epifanía
            "Epiphany": self.get_epiphany(),
            "Baptism of the Lord": self.get_baptism_of_the_lord(),
            
            # Tiempo de Cuaresma
            "Ash Wednesday": self.get_ash_wednesday(),
            "Lent": f"From {lent_start} to {lent_end}",
            
            # Semana Santa
            "Palm Sunday": self.get_palm_sunday(),
            "Holy Thursday": self.get_holy_thursday(),
            "Good Friday": self.get_good_friday(),
            "Holy Saturday": self.get_holy_saturday(),
            
            # Tiempo Pascual
            "Easter Sunday": self.get_easter_sunday(),
            "Ascension": self.get_ascension(),
            "Pentecost": self.get_pentecost(),
            "Trinity Sunday": self.get_trinity_sunday(),
            "Corpus Christi": self.get_corpus_christi(),
            
            # Tiempo Ordinario y fin del año
            "Christ the King": self.get_christ_the_king(),
            
            # Adviento y Navidad
            "Advent Sundays": advent_sundays,
            "Christmas": datetime.date(self.year, 12, 25)
        }
