from ..api.exceptions import RestApiException
from ..conf import conf
from ..models import PhoneCode
from ..utils import SmsService


class GeneratorService(SmsService):
    def __init__(self, phone_number: str, owner=None):
        self.phone_number = phone_number
        self.owner = owner

    def process(self):
        code = PhoneCode.objects\
            .filter(phone_number=self.phone_number)\
            .first()

        if code is not None:
            if not code.is_allow:
                raise RestApiException(detail={"detail": conf.SMS_WAIT_TIME})

            code.delete()

        PhoneCode.objects\
            .create(phone_number=self.phone_number,
                    owner=self.owner)
