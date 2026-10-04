# core/internationalization/english.py
# English locale configuration (v3.6.0)

"""
English Locale Configuration.

Primary locale for Project Foundation Template.

Official Resources:
- ISO 639-1: en
- IETF BCP 47: en, en-US, en-GB

Introduced in v3.6.0.
"""

LOCALE_ID = "en"

LOCALE = {
    "id": "en",
    "name": "English",
    "native_name": "English",
    "direction": "ltr",
    "script": "Latin",
    "variants": ["en-US", "en-GB", "en-AU", "en-CA"],
    "formats": {
        "date": "MM/DD/YYYY",
        "date_long": "MMMM D, YYYY",
        "time": "h:mm A",
        "datetime": "MM/DD/YYYY h:mm A",
        "number": {"decimal": ".", "thousands": ","},
    },
    "translations": {
        "common": {
            "yes": "Yes", "no": "No", "ok": "OK", "cancel": "Cancel",
            "save": "Save", "delete": "Delete", "edit": "Edit", "close": "Close",
            "loading": "Loading...", "error": "Error", "success": "Success", "warning": "Warning",
        },
        "governance": {
            "readme": "README", "contributing": "Contributing", "license": "License",
            "code_of_conduct": "Code of Conduct", "security_policy": "Security Policy", "changelog": "Changelog",
        },
        "errors": {
            "not_found": "Not found", "unauthorized": "Unauthorized",
            "validation_failed": "Validation failed", "server_error": "Server error",
        },
    },
}
