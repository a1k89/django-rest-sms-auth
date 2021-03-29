from django.contrib.auth import get_user_model

from ..api.exceptions import SMSCodeNotFoundException
from ..conf import conf
from ..models import \
    PhoneCode
from ..utils import SmsService

User = get_user_model()


class AuthService(SmsService):
    def __init__(self, phone_number: str, code: str):
        self.phone_number = phone_number
        self.code = code

        super().__init__()

    def process(self):
        generated_code = PhoneCode.objects.\
            filter(phone_number=self.phone_number,
                   code=self.code)\
            .first()

        if generated_code is None:
            raise SMSCodeNotFoundException()

        user = generated_code.owner
        kwargs = {conf.SMS_USER_FIELD: generated_code.phone_number}
        if user is None:
            user, created = User.objects.get_or_create(**kwargs,
                                                       defaults={"is_active": True})
        else:
            user.save(**kwargs)

        generated_code.delete()

        return user
