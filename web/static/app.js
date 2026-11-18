// Shared calculator for the static GitHub Pages front-end, in three languages.
// The page's <html lang="…"> selects the language; all asset and package paths
// are root-absolute so the same script works from /, /es/ and /fr/.

(function () {
    'use strict';

    // ----- Translations -----
    var I18N = {
        en: {
            errorPrefix: 'Error:',
            engineError: function (d) { return 'Could not load the calculation engine (' + d + '). Check your connection and reload.'; },
            invalidYear: 'Invalid year',
            noJulian: function (y) { return 'No Easter data available for Julian year ' + y + '.'; },
            calcError: 'Unexpected error during calculation.',
            yearWord: 'Year', calendarType: 'Calendar Type', leapYear: 'Leap Year',
            yes: 'Yes', no: 'No', julian: 'Julian', gregorian: 'Gregorian',
            liturgicalDates: 'Liturgical Dates', lentPeriod: 'Lent Period',
            lentRange: function (a, b) { return 'From ' + a + ' to ' + b; },
            adventSundays: 'Advent Sundays',
            feasts: {
                'Epiphany': 'Epiphany', 'Baptism of the Lord': 'Baptism of the Lord',
                'Ash Wednesday': 'Ash Wednesday', 'Palm Sunday': 'Palm Sunday',
                'Holy Thursday': 'Holy Thursday', 'Good Friday': 'Good Friday',
                'Holy Saturday': 'Holy Saturday', 'Easter Sunday': 'Easter Sunday',
                'Ascension': 'Ascension', 'Pentecost': 'Pentecost',
                'Trinity Sunday': 'Trinity Sunday', 'Corpus Christi': 'Corpus Christi',
                'Christ the King': 'Christ the King', 'Christmas': 'Christmas'
            }
        },
        es: {
            errorPrefix: 'Error:',
            engineError: function (d) { return 'No se pudo cargar el motor de cálculo (' + d + '). Revisa tu conexión y recarga.'; },
            invalidYear: 'Año no válido',
            noJulian: function (y) { return 'No hay datos de Pascua para el año juliano ' + y + '.'; },
            calcError: 'Error inesperado durante el cálculo.',
            yearWord: 'Año', calendarType: 'Tipo de calendario', leapYear: 'Año bisiesto',
            yes: 'Sí', no: 'No', julian: 'Juliano', gregorian: 'Gregoriano',
            liturgicalDates: 'Fechas litúrgicas', lentPeriod: 'Tiempo de Cuaresma',
            lentRange: function (a, b) { return 'Del ' + a + ' al ' + b; },
            adventSundays: 'Domingos de Adviento',
            feasts: {
                'Epiphany': 'Epifanía', 'Baptism of the Lord': 'Bautismo del Señor',
                'Ash Wednesday': 'Miércoles de Ceniza', 'Palm Sunday': 'Domingo de Ramos',
                'Holy Thursday': 'Jueves Santo', 'Good Friday': 'Viernes Santo',
                'Holy Saturday': 'Sábado Santo', 'Easter Sunday': 'Domingo de Pascua',
                'Ascension': 'Ascensión', 'Pentecost': 'Pentecostés',
                'Trinity Sunday': 'Domingo de la Santísima Trinidad', 'Corpus Christi': 'Corpus Christi',
                'Christ the King': 'Cristo Rey', 'Christmas': 'Navidad'
            }
        },
        fr: {
            errorPrefix: 'Erreur :',
            engineError: function (d) { return 'Impossible de charger le moteur de calcul (' + d + '). Vérifiez votre connexion et rechargez.'; },
            invalidYear: 'Année non valide',
            noJulian: function (y) { return "Aucune donnée de Pâques pour l'année julienne " + y + '.'; },
            calcError: 'Erreur inattendue pendant le calcul.',
            yearWord: 'Année', calendarType: 'Type de calendrier', leapYear: 'Année bissextile',
            yes: 'Oui', no: 'Non', julian: 'Julien', gregorian: 'Grégorien',
            liturgicalDates: 'Dates liturgiques', lentPeriod: 'Carême',
            lentRange: function (a, b) { return 'Du ' + a + ' au ' + b; },
            adventSundays: "Dimanches de l'Avent",
            feasts: {
                'Epiphany': 'Épiphanie', 'Baptism of the Lord': 'Baptême du Seigneur',
                'Ash Wednesday': 'Mercredi des Cendres', 'Palm Sunday': 'Dimanche des Rameaux',
                'Holy Thursday': 'Jeudi Saint', 'Good Friday': 'Vendredi Saint',
                'Holy Saturday': 'Samedi Saint', 'Easter Sunday': 'Dimanche de Pâques',
                'Ascension': 'Ascension', 'Pentecost': 'Pentecôte',
                'Trinity Sunday': 'Dimanche de la Trinité', 'Corpus Christi': 'Fête-Dieu',
                'Christ the King': 'Christ Roi', 'Christmas': 'Noël'
            }
        }
    };

    function getT() {
        var code = (document.documentElement.lang || 'en').slice(0, 2).toLowerCase();
        return I18N[code] || I18N.en;
    }
    var t = getT();

    // Metadata/special keys handled apart from the plain feast cards.
    var EXCLUDED_KEYS = ['Year', 'Calendar', 'Is Leap Year', 'Lent', 'Advent Sundays'];

    var statusEl = document.getElementById('engine-status');
    var buttonEl = document.getElementById('calc-button');
    var formEl = document.getElementById('calc-form');
    var errorSlot = document.getElementById('error-slot');
    var resultSlot = document.getElementById('result-slot');

    var computeFn = null;

    function escapeHtml(value) {
        return String(value).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    }

    function showError(message) {
        resultSlot.innerHTML = '';
        errorSlot.innerHTML = '<div class="error"><strong>' + t.errorPrefix + '</strong> ' + escapeHtml(message) + '</div>';
    }

    function reformatLent(value) {
        var m = String(value).match(/(\d{4}-\d{2}-\d{2})/g);
        return (m && m.length === 2) ? t.lentRange(m[0], m[1]) : value;
    }

    function render(result) {
        errorSlot.innerHTML = '';

        var calendar = result['Calendar'] === 'Julian' ? t.julian : t.gregorian;
        var leap = result['Is Leap Year'] ? t.yes : t.no;
        var cards = '';

        Object.keys(result).forEach(function (key) {
            if (EXCLUDED_KEYS.indexOf(key) !== -1) return;
            var label = t.feasts[key] || key;
            cards +=
                '<div class="date-card">' +
                    '<div class="date-label">' + escapeHtml(label) + '</div>' +
                    '<div class="date-value">' + escapeHtml(result[key]) + '</div>' +
                '</div>';
        });

        if ('Lent' in result) {
            cards +=
                '<div class="date-card">' +
                    '<div class="date-label">' + escapeHtml(t.lentPeriod) + '</div>' +
                    '<div class="date-value">' + escapeHtml(reformatLent(result['Lent'])) + '</div>' +
                '</div>';
        }

        if ('Advent Sundays' in result) {
            var list = '';
            result['Advent Sundays'].forEach(function (sunday, i) {
                list += (i + 1) + '. ' + escapeHtml(sunday) + '<br>';
            });
            cards +=
                '<div class="date-card advent-sundays">' +
                    '<div class="date-label">' + escapeHtml(t.adventSundays) + '</div>' +
                    '<div class="date-value">' + list + '</div>' +
                '</div>';
        }

        resultSlot.innerHTML =
            '<div class="result-section">' +
                '<div class="info-box">' +
                    '<h3>' + escapeHtml(t.yearWord) + ' ' + escapeHtml(result['Year']) + '</h3>' +
                    '<p><strong>' + escapeHtml(t.calendarType) + ':</strong> ' + escapeHtml(calendar) + '</p>' +
                    '<p><strong>' + escapeHtml(t.leapYear) + ':</strong> ' + escapeHtml(leap) + '</p>' +
                '</div>' +
                '<h2>' + escapeHtml(t.liturgicalDates) + '</h2>' +
                '<div class="dates-grid">' + cards + '</div>' +
            '</div>';
    }

    function translateError(payload) {
        switch (payload.error_code) {
            case 'invalid_year': return t.invalidYear;
            case 'no_julian_data': return t.noJulian(payload.year);
            default: return t.calcError;
        }
    }

    // Absolute base dir inside Pyodide's virtual filesystem. Absolute paths are
    // required: a relative path fails with ErrnoError/ENOENT.
    var PKG_BASE = '/lib_calendario';

    function loadPackage(pyodide) {
        return fetch('/pkg-manifest.json').then(function (r) { return r.json(); }).then(function (manifest) {
            pyodide.FS.mkdir(PKG_BASE);
            pyodide.FS.mkdir(PKG_BASE + '/calendario_liturgico');
            var chain = Promise.resolve();
            manifest.forEach(function (name) {
                chain = chain.then(function () {
                    return fetch('/calendario_liturgico/' + name).then(function (resp) {
                        if (!resp.ok) { throw new Error('Could not fetch ' + name + ' (HTTP ' + resp.status + ')'); }
                        return resp.text();
                    }).then(function (code) {
                        pyodide.FS.writeFile(PKG_BASE + '/calendario_liturgico/' + name, code);
                    });
                });
            });
            return chain.then(function () {
                pyodide.runPython("import sys\nif '" + PKG_BASE + "' not in sys.path:\n    sys.path.insert(0, '" + PKG_BASE + "')");
            });
        });
    }

    // The compute helper returns structured error codes so messages can be
    // localized in JS; the computed values (dates) are language-independent.
    var COMPUTE_SRC = [
        'import json, datetime',
        'from calendario_liturgico import LiturgicalCalendar',
        '',
        'def _compute(year_str):',
        '    try:',
        '        year = int(year_str)',
        '    except (ValueError, TypeError):',
        '        return json.dumps({"error_code": "invalid_year"})',
        '    try:',
        '        cal = LiturgicalCalendar(year)',
        '        dates = cal.get_all_dates()',
        '        out = {}',
        '        for key, value in dates.items():',
        '            if isinstance(value, list):',
        '                out[key] = [str(item) for item in value]',
        '            elif isinstance(value, datetime.date):',
        '                out[key] = str(value)',
        '            else:',
        '                out[key] = value',
        '        return json.dumps({"result": out})',
        '    except ValueError:',
        '        return json.dumps({"error_code": "no_julian_data", "year": year})',
        '    except Exception as exc:',
        '        return json.dumps({"error_code": "generic", "detail": str(exc)})',
        '',
        '_compute'
    ].join('\n');

    function boot() {
        loadPyodide({ indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/' })
            .then(function (pyodide) {
                return loadPackage(pyodide).then(function () {
                    computeFn = pyodide.runPython(COMPUTE_SRC);
                    try {
                        var version = pyodide.runPython('from calendario_liturgico import __version__\n__version__');
                        var el = document.getElementById('lib-version');
                        if (el) { el.textContent = 'v' + version; }
                    } catch (e) { /* cosmetic */ }
                    statusEl.textContent = '';
                    buttonEl.disabled = false;
                });
            })
            .catch(function (err) {
                statusEl.textContent = '';
                var detail = (err && err.message) ? err.message : String(err);
                showError(t.engineError(detail));
                if (window.console) { console.error(err); }
            });
    }

    formEl.addEventListener('submit', function (event) {
        event.preventDefault();
        if (!computeFn) { return; }
        var yearValue = document.getElementById('year').value;
        var payload;
        try {
            payload = JSON.parse(computeFn(yearValue));
        } catch (err) {
            showError(t.calcError);
            if (window.console) { console.error(err); }
            return;
        }
        if (payload.error_code) {
            showError(translateError(payload));
        } else {
            render(payload.result);
        }
    });

    boot();
})();
