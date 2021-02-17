import importlib

from django.conf import settings
from django.contrib.auth import get_user_model

SMS_AUTH_SETTINGS = getattr(settings, "SMS_AUTH_SETTINGS", {})

# SMS AUTH
SMS_AUTH_SETTINGS.setdefault("SMS_TIMELIFE", 60)
SMS_AUTH_SETTINGS.setdefault("SMS_USER_FIELD", "username")
SMS_AUTH_SETTINGS.setdefault("SMS_DEBUG", False)
SMS_AUTH_SETTINGS.setdefault("SMS_DEBUG_CODE", 1111)
SMS_AUTH_SETTINGS.setdefault("SMS_AUTH_CODE_LEN", 4)

# MESSAGES
SMS_AUTH_SETTINGS.setdefault("SMS_CODE_NOT_FOUND", "Code not found")
SMS_AUTH_SETTINGS.setdefault("SMS_WAIT_TIME", "Code was send early")
SMS_AUTH_SETTINGS.setdefault(
    "SMS_REQUEST_SUCCESS", "Your request was successfully processed"
)

# CELERY
SMS_AUTH_SETTINGS.setdefault("SMS_CELERY_FILE_NAME", "run_celery")

# Credentials
SMS_AUTH_SETTINGS.setdefault("SMS_AUTH_PROVIDER_LOGIN", "")
SMS_AUTH_SETTINGS.setdefault("SMS_AUTH_PROVIDER_PASSWORD", "")
SMS_AUTH_SETTINGS.setdefault("SMS_AUTH_PROVIDER_FROM", "")
SMS_AUTH_SETTINGS.setdefault("SMS_AUTH_PROVIDER_URL", "")

# Twilio
SMS_AUTH_SETTINGS.setdefault(
    "SMS_AUTH_ACCOUNT_SID", ""
)
SMS_AUTH_SETTINGS.setdefault("SMS_AUTH_AUTH_TOKEN", "")

# User model
SMS_AUTH_SETTINGS.setdefault("USER_MODEL", settings.AUTH_USER_MODEL)
SMS_AUTH_SETTINGS.setdefault("SMS_AUTH_SUCCESS_KEY", "jwt_token")

# Provider
for app in settings.INSTALLED_APPS:
    if "providers" in app:
        module = importlib.import_module(app)
        last_name = app.split(".")[-1]
        last_name.title()
        provider_class = getattr(module, last_name.title())
        SMS_AUTH_SETTINGS.setdefault("SMS_PROVIDER", provider_class)


class Conf:
    SMS_TIMELIFE = SMS_AUTH_SETTINGS.get("SMS_TIMELIFE")
    SMS_USER_FIELD = SMS_AUTH_SETTINGS.get("SMS_USER_FIELD")
    SMS_DEBUG = SMS_AUTH_SETTINGS.get("SMS_DEBUG")
    SMS_DEBUG_CODE = SMS_AUTH_SETTINGS.get("SMS_DEBUG_CODE")
    SMS_CODE_NOT_FOUND = SMS_AUTH_SETTINGS.get("SMS_CODE_NOT_FOUND")
    SMS_WAIT_TIME = SMS_AUTH_SETTINGS.get("SMS_WAIT_TIME")
    SMS_REQUEST_SUCCESS = SMS_AUTH_SETTINGS.get("SMS_REQUEST_SUCCESS")
    SMS_CELERY_FILE_NAME = SMS_AUTH_SETTINGS.get("SMS_CELERY_FILE_NAME")
    SMS_PROVIDER = SMS_AUTH_SETTINGS.get("SMS_PROVIDER")
    SMS_PROVIDER_LOGIN = SMS_AUTH_SETTINGS.get("SMS_AUTH_PROVIDER_LOGIN")
    SMS_PROVIDER_PASSWORD = SMS_AUTH_SETTINGS.get("SMS_AUTH_PROVIDER_PASSWORD")
    SMS_PROVIDER_FROM = SMS_AUTH_SETTINGS.get("SMS_AUTH_PROVIDER_FROM")
    SMS_PROVIDER_URL = SMS_AUTH_SETTINGS.get("SMS_AUTH_PROVIDER_URL")
    SMS_AUTH_ACCOUNT_SID = SMS_AUTH_SETTINGS.get("SMS_AUTH_ACCOUNT_SID")
    SMS_AUTH_AUTH_TOKEN = SMS_AUTH_SETTINGS.get("SMS_AUTH_AUTH_TOKEN")
    SMS_AUTH_CODE_LEN = SMS_AUTH_SETTINGS.get("SMS_AUTH_CODE_LEN")
    SMS_AUTH_SUCCESS_KEY = SMS_AUTH_SETTINGS.get("SMS_AUTH_SUCCESS_KEY")


conf = Conf()
