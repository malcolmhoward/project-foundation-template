# core/internationalization/spanish.py
# Spanish locale configuration (v3.6.0)

"""
Spanish Locale Configuration.

Official Resources:
- ISO 639-1: es
- IETF BCP 47: es, es-ES, es-MX, es-AR

Introduced in v3.6.0.
"""

LOCALE_ID = "es"

LOCALE = {
    "id": "es",
    "name": "Spanish",
    "native_name": "Español",
    "direction": "ltr",
    "script": "Latin",
    "variants": ["es-ES", "es-MX", "es-AR", "es-CO"],
    "formats": {
        "date": "DD/MM/YYYY",
        "date_long": "D de MMMM de YYYY",
        "time": "HH:mm",
        "datetime": "DD/MM/YYYY HH:mm",
        "number": {"decimal": ",", "thousands": "."},
    },
    "translations": {
        "common": {
            "yes": "Sí", "no": "No", "ok": "Aceptar", "cancel": "Cancelar",
            "save": "Guardar", "delete": "Eliminar", "edit": "Editar", "close": "Cerrar",
            "loading": "Cargando...", "error": "Error", "success": "Éxito", "warning": "Advertencia",
        },
        "governance": {
            "readme": "LÉAME", "contributing": "Contribuir", "license": "Licencia",
            "code_of_conduct": "Código de Conducta", "security_policy": "Política de Seguridad", "changelog": "Registro de Cambios",
        },
        "errors": {
            "not_found": "No encontrado", "unauthorized": "No autorizado",
            "validation_failed": "Validación fallida", "server_error": "Error del servidor",
        },
    },
}
