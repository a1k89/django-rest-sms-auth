import uuid

from django.db.models.signals import post_save
from django.db.transaction import on_commit
from django.dispatch import receiver

from .models import PhoneCode
from .tasks import send_sms_async


@receiver(post_save, sender=PhoneCode, dispatch_uid=uuid.uuid4())
def phone_code_post_save(sender, instance, created, **kwargs):
    if created:
        on_commit(lambda: send_sms_async.delay(instance.pk))
