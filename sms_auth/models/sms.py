from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

from phonenumber_field.modelfields import PhoneNumberField

from ..utils import random_code, valid_to


class SMSMessage(models.Model):
    """
    Save sended sms after as history
    """

    created = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField("Phone number", max_length=20)

    def __str__(self):
        return f"{self.phone_number} / {self.created}"

    def __repr__(self):
        return f"{self.phone_number}"

    class Meta:
        verbose_name = "Sms log"
        verbose_name_plural = "Sms log"


class PhoneCode(models.Model):
    """
    After validation save phone code instance
    """

    phone_number = PhoneNumberField(unique=True)
    owner = models.ForeignKey(get_user_model(),
                              null=True,
                              on_delete=models.CASCADE)
    code = models.PositiveIntegerField(default=random_code)
    valid_to = models.DateTimeField(default=valid_to)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("created_at",)
        verbose_name = "Phone code"
        verbose_name_plural = "Phone codes"

    def __str__(self):
        return f"{self.phone_number} ({self.code})"

    def __repr__(self):
        return self.__str__()

    @property
    def is_allow(self):
        return timezone.now() >= self.valid_to

    @property
    def message(self) -> str:
        return f"Your auth code: {self.code}"

    def save(self, *args, **kwargs):
        from ..conf import conf

        pretendent = self.__class__.objects.filter(
            phone_number=self.phone_number
        ).first()
        if pretendent is not None:
            self.pk = pretendent.pk

        if conf.SMS_AUTH_DEBUG_PHONE_NUMBER is not None:
            if self.phone_number == conf.SMS_AUTH_DEBUG_PHONE_NUMBER:
                self.code = conf.SMS_DEBUG_CODE

        super().save(*args, **kwargs)
