from django.contrib.admin import ModelAdmin, register

from .models import *


@register(SMSMessage)
class SMSMessageAdmin(ModelAdmin):
    readonly_fields = (
        "created",
        "phone_number",
    )

    def has_add_permission(self, request):
        return False


@register(PhoneCode)
class PhoneCodeAdmin(ModelAdmin):
    readonly_fields = (
        "valid_to",
        "created_at",
    )