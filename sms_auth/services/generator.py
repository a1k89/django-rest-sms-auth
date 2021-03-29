from django.contrib.auth import get_user_model

from ..api.exceptions import \
    SMSWaitException, \
    UserAlreadyExistException

from ..models import PhoneCode
from ..utils import SmsService
from ..conf import conf


class GeneratorService(SmsService):
    def __init__(self, phone_number: str, owner=None):
        self.phone_number = phone_number
        self.owner = owner

    def process(self):
        if self.owner is not None:
            code = PhoneCode.objects\
                .filter(owner=self.owner)\
                .first()
        else:
            code = PhoneCode.objects\
                .filter(phone_number=self.phone_number)\
                .first()

        if code is not None:
            if not code.is_allow:
                raise SMSWaitException()

            code.delete()

        if self.owner is not None:
            kwargs = {conf.SMS_USER_FIELD: self.phone_number}
            if get_user_model().objects.filter(**kwargs).exists():
                raise UserAlreadyExistException()

        PhoneCode.objects\
            .create(phone_number=self.phone_number,
                    owner=self.owner)
