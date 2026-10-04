# core/internationalization/hindi.py
# Hindi locale configuration (v3.6.0)

"""
Hindi Locale Configuration.

Note on terminology: Hindi (हिन्दी) is one of India's official languages,
written in the Devanagari script (देवनागरी). India has 22 scheduled languages;
Hindi is the most widely spoken. This locale uses standard Hindi as used in
formal and digital contexts.

Official Resources:
- ISO 639-1: hi
- IETF BCP 47: hi, hi-IN

Introduced in v3.6.0.
"""

LOCALE_ID = "hi"

LOCALE = {
    "id": "hi",
    "name": "Hindi",
    "native_name": "हिन्दी",
    "direction": "ltr",
    "script": "Devanagari",
    "variants": ["hi-IN"],
    "formats": {
        "date": "DD/MM/YYYY",
        "date_long": "D MMMM YYYY",
        "time": "h:mm A",
        "datetime": "DD/MM/YYYY h:mm A",
        "number": {"decimal": ".", "thousands": ","},
        "number_indian": {"pattern": "##,##,###"},
    },
    "translations": {
        "common": {
            "yes": "हाँ", "no": "नहीं", "ok": "ठीक है", "cancel": "रद्द करें",
            "save": "सहेजें", "delete": "हटाएं", "edit": "संपादित करें", "close": "बंद करें",
            "loading": "लोड हो रहा है...", "error": "त्रुटि", "success": "सफलता", "warning": "चेतावनी",
        },
        "governance": {
            "readme": "पढ़ें", "contributing": "योगदान", "license": "लाइसेंस",
            "code_of_conduct": "आचार संहिता", "security_policy": "सुरक्षा नीति", "changelog": "परिवर्तन लॉग",
        },
        "errors": {
            "not_found": "नहीं मिला", "unauthorized": "अनधिकृत",
            "validation_failed": "सत्यापन विफल", "server_error": "सर्वर त्रुटि",
        },
    },
}
