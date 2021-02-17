from django.apps import AppConfig


class SmsConfig(AppConfig):
    name = "sms_auth"
    verbose_name = "SMS auth"

    def ready(self):
        from sms_auth.listeners import phone_code_post_save
