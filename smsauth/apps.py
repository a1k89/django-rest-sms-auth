from django.apps import AppConfig


class SmsConfig(AppConfig):
    name = "smsauth"
    verbose_name = "SMS auth"

    def ready(self):
        from smsauth.listeners import phone_code_post_save
