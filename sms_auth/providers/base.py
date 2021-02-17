from typing import Protocol


def sms_decorator(func, to):
    from ..models import SMSMessage

    def wrapper():
        result = func()
        if result:
            SMSMessage.objects.create(phone_number=to)

    return wrapper


class SMSProviderClass(Protocol):
    to: str
    message: str
    conf: dict

    def send_sms(self) -> None:
        pass


class SMSProvider:
    def __getattribute__(self, item):
        element = super().__getattribute__(item)
        if callable(element) and item == "send_sms":
            return sms_decorator(element, self.to)

        return element

    def __init__(self, to, message, conf):
        self.to = to
        self.message = message
        self.conf = conf

    def send_sms(self) -> str:
        raise NotImplementedError()
