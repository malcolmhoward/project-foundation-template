# core/internationalization/japanese.py
# Japanese locale configuration (v3.6.0)

"""
Japanese Locale Configuration.

Note on writing system: Japanese uses three scripts - Kanji (漢字, Chinese
characters), Hiragana (ひらがな), and Katakana (カタカナ). This locale
configuration handles the standard written Japanese language.

Official Resources:
- ISO 639-1: ja
- IETF BCP 47: ja, ja-JP

Introduced in v3.6.0.
"""

LOCALE_ID = "ja"

LOCALE = {
    "id": "ja",
    "name": "Japanese",
    "native_name": "日本語",
    "direction": "ltr",
    "script": "Japanese",  # Combination of Kanji, Hiragana, Katakana
    "variants": ["ja-JP"],
    "formats": {
        "date": "YYYY/MM/DD",
        "date_long": "YYYY年M月D日",
        "time": "HH:mm",
        "datetime": "YYYY/MM/DD HH:mm",
        "number": {"decimal": ".", "thousands": ","},
    },
    "translations": {
        "common": {
            "yes": "はい", "no": "いいえ", "ok": "OK", "cancel": "キャンセル",
            "save": "保存", "delete": "削除", "edit": "編集", "close": "閉じる",
            "loading": "読み込み中...", "error": "エラー", "success": "成功", "warning": "警告",
        },
        "governance": {
            "readme": "はじめに", "contributing": "貢献ガイド", "license": "ライセンス",
            "code_of_conduct": "行動規範", "security_policy": "セキュリティポリシー", "changelog": "変更履歴",
        },
        "errors": {
            "not_found": "見つかりません", "unauthorized": "認証されていません",
            "validation_failed": "検証に失敗しました", "server_error": "サーバーエラー",
        },
    },
}
