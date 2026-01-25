# core/internationalization/chinese.py
# Chinese locale configuration (v3.6.0)

"""
Chinese Locale Configuration.

Note on terminology: "Chinese" (中文) refers to the written language system,
which is shared across spoken varieties including Mandarin (普通话), Cantonese
(粤语), and others. This locale configuration handles the written language
with support for both Simplified (简体) and Traditional (繁體) scripts.

Official Resources:
- ISO 639-1: zh
- IETF BCP 47: zh, zh-CN (Simplified), zh-TW (Traditional)

Introduced in v3.6.0.
"""

LOCALE_ID = "zh"

LOCALE = {
    "id": "zh",
    "name": "Chinese",
    "native_name": "中文",
    "direction": "ltr",
    "script": "Han",
    "variants": ["zh-CN", "zh-TW", "zh-HK"],
    # Script variants for written Chinese
    "scripts": {
        "simplified": "zh-Hans",  # Used in Mainland China, Singapore
        "traditional": "zh-Hant",  # Used in Taiwan, Hong Kong, Macau
    },
    "formats": {
        "date": "YYYY/MM/DD",
        "date_long": "YYYY年M月D日",
        "time": "HH:mm",
        "datetime": "YYYY/MM/DD HH:mm",
        "number": {"decimal": ".", "thousands": ","},
    },
    # Translations in Simplified Chinese (简体中文)
    "translations": {
        "common": {
            "yes": "是", "no": "否", "ok": "确定", "cancel": "取消",
            "save": "保存", "delete": "删除", "edit": "编辑", "close": "关闭",
            "loading": "加载中...", "error": "错误", "success": "成功", "warning": "警告",
        },
        "governance": {
            "readme": "自述文件", "contributing": "贡献指南", "license": "许可证",
            "code_of_conduct": "行为准则", "security_policy": "安全政策", "changelog": "更新日志",
        },
        "errors": {
            "not_found": "未找到", "unauthorized": "未授权",
            "validation_failed": "验证失败", "server_error": "服务器错误",
        },
    },
}
