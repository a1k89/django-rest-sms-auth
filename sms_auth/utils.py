import random
from abc import ABC, abstractmethod
from datetime import timedelta

from django.db import transaction
from django.utils import timezone


class SmsService(ABC):
    @classmethod
    def execute(cls, **kwargs):
        instance = cls(**kwargs)
        with transaction.atomic():
            return instance.process()

    @abstractmethod
    def process(self):
        pass


def valid_to():
    from .conf import conf

    now = timezone.now()
    delta = conf.SMS_TIMELIFE
    due_at = now + timedelta(seconds=delta)

    return due_at


def random_n(n) -> int:
    range_start = 10 ** (n - 1)
    range_finish = (10 ** n) - 1

    return random.randint(range_start, range_finish)


def random_code() -> int:
    from .conf import conf

    code = random_n(conf.SMS_AUTH_CODE_LEN)

    if conf.SMS_DEBUG:
        code = conf.SMS_DEBUG_CODE

    return code
