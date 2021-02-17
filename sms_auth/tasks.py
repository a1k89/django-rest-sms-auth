import importlib

from .conf import conf
from .models import PhoneCode


celery_conf = importlib.import_module(conf.SMS_CELERY_FILE_NAME)
app = getattr(celery_conf, "app")


def get_provider_class():
    provider = conf.SMS_PROVIDER

    return provider


@app.task
def send_sms_async(identifier: int):
    code_instance = PhoneCode.objects.filter(pk=identifier).first()
    if code_instance:
        provider_class = get_provider_class()
        provider = provider_class(
            to=code_instance.phone_number, message=code_instance.message, conf=conf
        )
        provider.send_sms()
