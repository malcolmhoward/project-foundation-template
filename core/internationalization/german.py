# core/internationalization/german.py
# German locale configuration (v3.6.0)

"""
German Locale Configuration.

Official Resources:
- ISO 639-1: de
- IETF BCP 47: de, de-DE, de-AT, de-CH

Introduced in v3.6.0.
"""

LOCALE_ID = "de"

LOCALE = {
    "id": "de",
    "name": "German",
    "native_name": "Deutsch",
    "direction": "ltr",
    "script": "Latin",
    "variants": ["de-DE", "de-AT", "de-CH"],
    "formats": {
        "date": "DD.MM.YYYY",
        "date_long": "D. MMMM YYYY",
        "time": "HH:mm",
        "datetime": "DD.MM.YYYY HH:mm",
        "number": {"decimal": ",", "thousands": "."},
    },
    "translations": {
        "common": {
            "yes": "Ja", "no": "Nein", "ok": "OK", "cancel": "Abbrechen",
            "save": "Speichern", "delete": "Löschen", "edit": "Bearbeiten", "close": "Schließen",
            "loading": "Laden...", "error": "Fehler", "success": "Erfolg", "warning": "Warnung",
        },
        "governance": {
            "readme": "LIES-MICH", "contributing": "Mitwirken", "license": "Lizenz",
            "code_of_conduct": "Verhaltenskodex", "security_policy": "Sicherheitsrichtlinie", "changelog": "Änderungsprotokoll",
        },
        "errors": {
            "not_found": "Nicht gefunden", "unauthorized": "Nicht autorisiert",
            "validation_failed": "Validierung fehlgeschlagen", "server_error": "Serverfehler",
        },
    },
}
