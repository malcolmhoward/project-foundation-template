# core/internationalization/korean.py
# Korean locale configuration (v3.6.0)

"""
Korean Locale Configuration.

Official Resources:
- ISO 639-1: ko
- IETF BCP 47: ko, ko-KR

Introduced in v3.6.0.
"""

LOCALE_ID = "ko"

LOCALE = {
    "id": "ko",
    "name": "Korean",
    "native_name": "한국어",
    "direction": "ltr",
    "script": "Hangul",
    "variants": ["ko-KR"],
    "formats": {
        "date": "YYYY. MM. DD.",
        "date_long": "YYYY년 M월 D일",
        "time": "HH:mm",
        "datetime": "YYYY. MM. DD. HH:mm",
        "number": {"decimal": ".", "thousands": ","},
    },
    "translations": {
        "common": {
            "yes": "예", "no": "아니오", "ok": "확인", "cancel": "취소",
            "save": "저장", "delete": "삭제", "edit": "편집", "close": "닫기",
            "loading": "로딩 중...", "error": "오류", "success": "성공", "warning": "경고",
        },
        "governance": {
            "readme": "읽어보기", "contributing": "기여 가이드", "license": "라이선스",
            "code_of_conduct": "행동 강령", "security_policy": "보안 정책", "changelog": "변경 기록",
        },
        "errors": {
            "not_found": "찾을 수 없음", "unauthorized": "인증되지 않음",
            "validation_failed": "유효성 검사 실패", "server_error": "서버 오류",
        },
    },
}
