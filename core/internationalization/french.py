# core/internationalization/french.py
# French locale configuration (v3.6.0)

"""
French Locale Configuration.

Official Resources:
- ISO 639-1: fr
- IETF BCP 47: fr, fr-FR, fr-CA, fr-BE

Introduced in v3.6.0.
"""

LOCALE_ID = "fr"

LOCALE = {
    "id": "fr",
    "name": "French",
    "native_name": "Français",
    "direction": "ltr",
    "script": "Latin",
    "variants": ["fr-FR", "fr-CA", "fr-BE", "fr-CH"],
    "formats": {
        "date": "DD/MM/YYYY",
        "date_long": "D MMMM YYYY",
        "time": "HH:mm",
        "datetime": "DD/MM/YYYY HH:mm",
        "number": {"decimal": ",", "thousands": " "},
    },
    "translations": {
        "common": {
            "yes": "Oui", "no": "Non", "ok": "OK", "cancel": "Annuler",
            "save": "Enregistrer", "delete": "Supprimer", "edit": "Modifier", "close": "Fermer",
            "loading": "Chargement...", "error": "Erreur", "success": "Succès", "warning": "Avertissement",
        },
        "governance": {
            "readme": "LISEZ-MOI", "contributing": "Contribuer", "license": "Licence",
            "code_of_conduct": "Code de Conduite", "security_policy": "Politique de Sécurité", "changelog": "Journal des Modifications",
        },
        "errors": {
            "not_found": "Non trouvé", "unauthorized": "Non autorisé",
            "validation_failed": "Échec de validation", "server_error": "Erreur serveur",
        },
    },
}
