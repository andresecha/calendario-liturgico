# Liturgical Calendar / Calendario Litúrgico / Calendrier Liturgique

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![License: Etalab-2.0](https://img.shields.io/badge/License-Etalab--2.0-blue.svg)](https://www.etalab.gouv.fr/wp-content/uploads/2017/04/ETALAB-Licence-Ouverte-v2.0.pdf)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)](https://github.com/andresecha/calendario-liturgico)

[English](#english) | [Español](#español) | [Français](#français)

---

## English

A Python library for calculating Christian liturgical dates in both Julian and Gregorian calendars.

### Features

- ✅ Julian calendar support (years 532-1582)
- ✅ Gregorian calendar support (years 1583+)
- ✅ Cross-platform (Windows, Linux, macOS)
- ✅ No special characters in function names (no ñ, no accents)
- ✅ Fully type-hinted
- ✅ No external dependencies (core library)
- ✅ Etalab Open License 2.0 (free for commercial use)
- ✅ Web interface for testing with experts

### Installation

#### Option 1: From PyPI (when published)

```bash
pip install calendario-liturgico
```

#### Option 2: Local Installation

**Windows:**
```cmd
git clone https://github.com/andresecha/calendario-liturgico.git
cd calendario-liturgico
install_local.bat
```

**Linux/macOS:**
```bash
git clone https://github.com/andresecha/calendario-liturgico.git
cd calendario-liturgico
chmod +x install_local.sh
./install_local.sh
```

### Quick Start

```python
from calendario_liturgico import LiturgicalCalendar

# Create calendar for 2024
cal = LiturgicalCalendar(2024)

# Get liturgical dates
print(cal.get_easter_sunday())      # 2024-03-31
print(cal.get_ash_wednesday())      # 2024-02-14
print(cal.get_pentecost())          # 2024-05-19
print(cal.get_corpus_christi())     # 2024-05-30

# Get all dates at once
all_dates = cal.get_all_dates()
for event, date in all_dates.items():
    print(f"{event}: {date}")
```

### Web Interface for Testing

Perfect for validation with liturgical experts:

**Windows:**
```cmd
cd web
python app.py
```

**Linux/macOS:**
```bash
cd web
python3 app.py
```

Then open http://localhost:5000 in your browser.

### API Reference

All method names are in English without special characters:

#### Main Methods

- `get_easter_sunday()` - Easter Sunday
- `get_ash_wednesday()` - Ash Wednesday (start of Lent)
- `get_palm_sunday()` - Palm Sunday
- `get_holy_thursday()` - Holy Thursday / Maundy Thursday
- `get_good_friday()` - Good Friday
- `get_holy_saturday()` - Holy Saturday
- `get_pentecost()` - Pentecost (49 days after Easter)
- `get_ascension()` - Ascension (39 days after Easter)
- `get_trinity_sunday()` - Trinity Sunday
- `get_corpus_christi()` - Corpus Christi
- `get_epiphany()` - Epiphany (January 6)
- `get_baptism_of_the_lord()` - Baptism of the Lord
- `get_advent_start()` - First Sunday of Advent
- `get_advent_sundays()` - All four Sundays of Advent (returns list)
- `get_christ_the_king()` - Christ the King (last Sunday before Advent)
- `get_lent_range()` - Lent period (returns tuple: start, end)
- `get_all_dates()` - Dictionary with all liturgical dates

#### Utility Functions

```python
from calendario_liturgico import is_leap_year, calculate_gregorian_easter

# Check if year is leap
is_leap_year(2024)                    # True
is_leap_year(1900)                    # False (Gregorian)
is_leap_year(1900, is_julian=True)    # True (Julian)

# Calculate Easter for Gregorian calendar
calculate_gregorian_easter(2025)      # datetime.date(2025, 4, 20)
```

### Running Tests

```bash
pytest
```

### License

Etalab Open License 2.0 - Free for commercial and non-commercial use with attribution requirement. Compatible with Creative Commons Attribution (CC-BY).

---

## Español

Una librería Python para calcular fechas del calendario litúrgico cristiano en calendarios juliano y gregoriano.

### Características

- ✅ Soporte para calendario juliano (años 532-1582)
- ✅ Soporte para calendario gregoriano (años 1583+)
- ✅ Multiplataforma (Windows, Linux, macOS)
- ✅ Sin caracteres especiales en nombres de funciones (sin ñ, sin acentos)
- ✅ Completamente documentado con type hints
- ✅ Sin dependencias externas (librería base)
- ✅ Licencia Abierta Etalab 2.0 (libre para uso comercial)
- ✅ Interfaz web para pruebas con expertos

### Instalación

#### Opción 1: Desde PyPI (cuando se publique)

```bash
pip install calendario-liturgico
```

#### Opción 2: Instalación Local

**Windows:**
```cmd
git clone https://github.com/andresecha/calendario-liturgico.git
cd calendario-liturgico
install_local.bat
```

**Linux/macOS:**
```bash
git clone https://github.com/andresecha/calendario-liturgico.git
cd calendario-liturgico
chmod +x install_local.sh
./install_local.sh
```

### Uso Rápido

```python
from calendario_liturgico import LiturgicalCalendar

# Crear calendario para 2024
cal = LiturgicalCalendar(2024)

# Obtener fechas litúrgicas
print(cal.get_easter_sunday())      # 2024-03-31
print(cal.get_ash_wednesday())      # 2024-02-14
print(cal.get_pentecost())          # 2024-05-19
print(cal.get_corpus_christi())     # 2024-05-30

# Obtener todas las fechas de una vez
todas_fechas = cal.get_all_dates()
for evento, fecha in todas_fechas.items():
    print(f"{evento}: {fecha}")
```

### Interfaz Web para Pruebas

Perfecta para validación con expertos litúrgicos:

**Windows:**
```cmd
cd web
python app.py
```

**Linux/macOS:**
```bash
cd web
python3 app.py
```

Luego abre http://localhost:5000 en tu navegador.

### Referencia de API

Todos los nombres de métodos están en inglés sin caracteres especiales:

#### Métodos Principales

- `get_easter_sunday()` - Domingo de Pascua
- `get_ash_wednesday()` - Miércoles de Ceniza (inicio de Cuaresma)
- `get_palm_sunday()` - Domingo de Ramos
- `get_holy_thursday()` - Jueves Santo
- `get_good_friday()` - Viernes Santo
- `get_holy_saturday()` - Sábado Santo
- `get_pentecost()` - Pentecostés (49 días después de Pascua)
- `get_ascension()` - Ascensión (39 días después de Pascua)
- `get_trinity_sunday()` - Domingo de la Trinidad
- `get_corpus_christi()` - Corpus Christi
- `get_epiphany()` - Epifanía (6 de enero)
- `get_baptism_of_the_lord()` - Bautismo del Señor
- `get_advent_start()` - Primer Domingo de Adviento
- `get_advent_sundays()` - Los cuatro Domingos de Adviento (devuelve lista)
- `get_christ_the_king()` - Cristo Rey (último domingo antes del Adviento)
- `get_lent_range()` - Período de Cuaresma (devuelve tupla: inicio, fin)
- `get_all_dates()` - Diccionario con todas las fechas litúrgicas

#### Funciones Auxiliares

```python
from calendario_liturgico import is_leap_year, calculate_gregorian_easter

# Verificar si el año es bisiesto
is_leap_year(2024)                    # True
is_leap_year(1900)                    # False (Gregoriano)
is_leap_year(1900, is_julian=True)    # True (Juliano)

# Calcular Pascua para calendario gregoriano
calculate_gregorian_easter(2025)      # datetime.date(2025, 4, 20)
```

### Ejecutar Tests

```bash
pytest
```

### Licencia

Licencia Abierta Etalab 2.0 - Libre para uso comercial y no comercial con requisito de atribución. Compatible con Creative Commons Attribution (CC-BY).

---

## Français

Une bibliothèque Python pour calculer les dates du calendrier liturgique chrétien dans les calendriers julien et grégorien.

### Caractéristiques

- ✅ Support du calendrier julien (années 532-1582)
- ✅ Support du calendrier grégorien (années 1583+)
- ✅ Multiplateforme (Windows, Linux, macOS)
- ✅ Aucun caractère spécial dans les noms de fonctions (pas de ñ, pas d'accents)
- ✅ Entièrement documenté avec type hints
- ✅ Aucune dépendance externe (bibliothèque de base)
- ✅ Licence Ouverte Etalab 2.0 (libre pour usage commercial)
- ✅ Interface web pour tests avec des experts

### Installation

#### Option 1: Depuis PyPI (quand publié)

```bash
pip install calendario-liturgico
```

#### Option 2: Installation Locale

**Windows:**
```cmd
git clone https://github.com/andresecha/calendario-liturgico.git
cd calendario-liturgico
install_local.bat
```

**Linux/macOS:**
```bash
git clone https://github.com/andresecha/calendario-liturgico.git
cd calendario-liturgico
chmod +x install_local.sh
./install_local.sh
```

### Démarrage Rapide

```python
from calendario_liturgico import LiturgicalCalendar

# Créer calendrier pour 2024
cal = LiturgicalCalendar(2024)

# Obtenir les dates liturgiques
print(cal.get_easter_sunday())      # 2024-03-31
print(cal.get_ash_wednesday())      # 2024-02-14
print(cal.get_pentecost())          # 2024-05-19
print(cal.get_corpus_christi())     # 2024-05-30

# Obtenir toutes les dates en une fois
toutes_dates = cal.get_all_dates()
for evenement, date in toutes_dates.items():
    print(f"{evenement}: {date}")
```

### Interface Web pour Tests

Parfaite pour la validation avec des experts liturgiques:

**Windows:**
```cmd
cd web
python app.py
```

**Linux/macOS:**
```bash
cd web
python3 app.py
```

Puis ouvrez http://localhost:5000 dans votre navigateur.

### Référence API

Tous les noms de méthodes sont en anglais sans caractères spéciaux:

#### Méthodes Principales

- `get_easter_sunday()` - Dimanche de Pâques
- `get_ash_wednesday()` - Mercredi des Cendres (début du Carême)
- `get_palm_sunday()` - Dimanche des Rameaux
- `get_holy_thursday()` - Jeudi Saint
- `get_good_friday()` - Vendredi Saint
- `get_holy_saturday()` - Samedi Saint
- `get_pentecost()` - Pentecôte (49 jours après Pâques)
- `get_ascension()` - Ascension (39 jours après Pâques)
- `get_trinity_sunday()` - Dimanche de la Trinité
- `get_corpus_christi()` - Fête-Dieu (Corpus Christi)
- `get_epiphany()` - Épiphanie (6 janvier)
- `get_baptism_of_the_lord()` - Baptême du Seigneur
- `get_advent_start()` - Premier Dimanche de l'Avent
- `get_advent_sundays()` - Les quatre Dimanches de l'Avent (retourne liste)
- `get_christ_the_king()` - Christ Roi (dernier dimanche avant l'Avent)
- `get_lent_range()` - Période du Carême (retourne tuple: début, fin)
- `get_all_dates()` - Dictionnaire avec toutes les dates liturgiques

#### Fonctions Utilitaires

```python
from calendario_liturgico import is_leap_year, calculate_gregorian_easter

# Vérifier si l'année est bissextile
is_leap_year(2024)                    # True
is_leap_year(1900)                    # False (Grégorien)
is_leap_year(1900, is_julian=True)    # True (Julien)

# Calculer Pâques pour calendrier grégorien
calculate_gregorian_easter(2025)      # datetime.date(2025, 4, 20)
```

### Exécuter les Tests

```bash
pytest
```

### Licence

Licence Ouverte Etalab 2.0 - Libre pour usage commercial et non commercial avec exigence d'attribution. Compatible avec Creative Commons Attribution (CC-BY).

---

## For Historians / Para Historiadores / Pour les Historiens

**EN:** This library is designed specifically for historians working with historical documents that use liturgical dates. The web interface allows easy validation of calculations with liturgical experts.

**ES:** Esta biblioteca está diseñada específicamente para historiadores que trabajan con documentos históricos que utilizan fechas litúrgicas. La interfaz web permite una fácil validación de cálculos con expertos litúrgicos.

**FR:** Cette bibliothèque est conçue spécifiquement pour les historiens travaillant avec des documents historiques utilisant des dates liturgiques. L'interface web permet une validation facile des calculs avec des experts liturgiques.

---

## Technical Details / Detalles Técnicos / Détails Techniques

### Platform Support / Soporte de Plataformas / Support de Plateformes

| Platform | Installation | Web Server |
|----------|-------------|------------|
| **Windows** | `install_local.bat` | `python app.py` |
| **Linux** | `./install_local.sh` | `python3 app.py` |
| **macOS** | `./install_local.sh` | `python3 app.py` |

### Requirements / Requisitos / Exigences

- Python 3.8 or higher / o superior / ou supérieur
- pip (included with Python / incluido con Python / inclus avec Python)
- Optional: Flask 3.0+ for web interface / Opcional: Flask 3.0+ para interfaz web / Optionnel: Flask 3.0+ pour interface web

### Data Range / Rango de Datos / Plage de Données

- **Julian Calendar / Calendario Juliano / Calendrier Julien**: Years 532-1582
- **Gregorian Calendar / Calendario Gregoriano / Calendrier Grégorien**: Years 1583+

---

## Contributing / Contribuir / Contribuer

**EN:** Contributions are welcome! Please ensure:
- All function/method names in English
- No special characters (ñ, accents) in code
- Add tests for new functionality
- Update documentation in all three languages

**ES:** ¡Las contribuciones son bienvenidas! Por favor asegurar:
- Todos los nombres de funciones/métodos en inglés
- Sin caracteres especiales (ñ, acentos) en el código
- Agregar tests para nueva funcionalidad
- Actualizar documentación en los tres idiomas

**FR:** Les contributions sont les bienvenues! Veuillez vous assurer:
- Tous les noms de fonctions/méthodes en anglais
- Aucun caractère spécial (ñ, accents) dans le code
- Ajouter des tests pour les nouvelles fonctionnalités
- Mettre à jour la documentation dans les trois langues

---

## Author / Autor / Auteur

Andres Felipe Echavarria Pelaez

## Version

0.0.1.2

## License / Licencia / Licence

Etalab Open License 2.0 / Licence Ouverte Etalab 2.0 - See LICENSE file for details
