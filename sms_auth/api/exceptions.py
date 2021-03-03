from rest_framework import serializers

from ..conf import conf


def get_error(error_message):
    ERROR = {
        'message': '',
        'errors': [
            {
                "code": "0000",
                "field": None,
                "message": error_message
            }
        ]
    }

    return ERROR


class RestApiException(serializers.ValidationError):
    status_code = 400
    default_detail = ""
    detail = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.detail = self.default_detail


class SMSWaitException(RestApiException):
    default_detail = detail = get_error(conf.SMS_WAIT_TIME)


class UserAlreadyExistException(RestApiException):
    default_detail = detail = get_error(conf.SMS_USER_ALREADY_EXIST)


class SMSCodeNotFoundException(RestApiException):
    default_detail = detail = get_error(conf.SMS_CODE_NOT_FOUND)
