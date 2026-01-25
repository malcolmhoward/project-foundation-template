# core/internationalization/arabic.py
# Arabic locale configuration (v3.6.0)

"""
Arabic Locale Configuration.

Note on terminology: "Arabic" (العربية) here refers to Modern Standard Arabic
(MSA/الفصحى), the formal written language used across the Arab world. Spoken
Arabic varies significantly by region (Egyptian, Levantine, Gulf, Maghrebi, etc.),
but MSA is the standard for written content and software localization.

This is a Right-to-Left (RTL) language requiring special handling
for text direction and layout.

Official Resources:
- ISO 639-1: ar
- IETF BCP 47: ar, ar-SA, ar-EG, ar-AE

Introduced in v3.6.0.
"""

LOCALE_ID = "ar"

LOCALE = {
    "id": "ar",
    "name": "Arabic",
    "native_name": "العربية",
    "direction": "rtl",
    "script": "Arabic",
    "variants": ["ar-SA", "ar-EG", "ar-AE", "ar-MA"],
    "rtl": {"enabled": True, "mirror_layout": True, "text_align": "right"},
    "formats": {
        "date": "DD/MM/YYYY",
        "date_long": "D MMMM YYYY",
        "time": "HH:mm",
        "datetime": "DD/MM/YYYY HH:mm",
        "number": {"decimal": "٫", "thousands": "٬"},
        "number_western": {"decimal": ".", "thousands": ","},
    },
    "translations": {
        "common": {
            "yes": "نعم", "no": "لا", "ok": "موافق", "cancel": "إلغاء",
            "save": "حفظ", "delete": "حذف", "edit": "تعديل", "close": "إغلاق",
            "loading": "جاري التحميل...", "error": "خطأ", "success": "نجاح", "warning": "تحذير",
        },
        "governance": {
            "readme": "اقرأني", "contributing": "المساهمة", "license": "الرخصة",
            "code_of_conduct": "قواعد السلوك", "security_policy": "سياسة الأمان", "changelog": "سجل التغييرات",
        },
        "errors": {
            "not_found": "غير موجود", "unauthorized": "غير مصرح",
            "validation_failed": "فشل التحقق", "server_error": "خطأ في الخادم",
        },
    },
}
