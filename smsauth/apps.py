from django.apps import AppConfig


class SmsConfig(AppConfig):
    name = "apps.smsauth"
    verbose_name = "SMS auth"

    def ready(self):
        from apps.smsauth.listeners import phone_code_post_save
