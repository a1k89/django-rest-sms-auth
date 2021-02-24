from django.contrib.auth import get_user_model

from ..api.exceptions import RestApiException
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
            raise RestApiException(detail={"detail": conf.SMS_CODE_NOT_FOUND})

        user = generated_code.owner
        if user is None:
            user, created = User.objects.get_or_create(
                username=generated_code.phone_number,
                defaults={"is_active": True}
            )

        user.username = generated_code.phone_number
        user.save()

        generated_code.delete()

        return user
