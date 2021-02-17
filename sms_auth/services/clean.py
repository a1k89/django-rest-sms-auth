from django.utils import timezone
from ..models import PhoneCode


class CleanService:
    @classmethod
    def clear(cls):
        PhoneCode.objects\
            .filter(valid_to__lt=timezone.now())\
            .delete()
