# core/internationalization/portuguese.py
# Portuguese locale configuration (v3.6.0)

"""
Portuguese Locale Configuration.

Official Resources:
- ISO 639-1: pt
- IETF BCP 47: pt, pt-BR, pt-PT

Introduced in v3.6.0.
"""

LOCALE_ID = "pt"

LOCALE = {
    "id": "pt",
    "name": "Portuguese",
    "native_name": "Português",
    "direction": "ltr",
    "script": "Latin",
    "variants": ["pt-BR", "pt-PT"],
    "formats": {
        "date": "DD/MM/YYYY",
        "date_long": "D de MMMM de YYYY",
        "time": "HH:mm",
        "datetime": "DD/MM/YYYY HH:mm",
        "number": {"decimal": ",", "thousands": "."},
    },
    "translations": {
        "common": {
            "yes": "Sim", "no": "Não", "ok": "OK", "cancel": "Cancelar",
            "save": "Salvar", "delete": "Excluir", "edit": "Editar", "close": "Fechar",
            "loading": "Carregando...", "error": "Erro", "success": "Sucesso", "warning": "Aviso",
        },
        "governance": {
            "readme": "LEIA-ME", "contributing": "Contribuindo", "license": "Licença",
            "code_of_conduct": "Código de Conduta", "security_policy": "Política de Segurança", "changelog": "Registro de Alterações",
        },
        "errors": {
            "not_found": "Não encontrado", "unauthorized": "Não autorizado",
            "validation_failed": "Falha na validação", "server_error": "Erro no servidor",
        },
    },
}
