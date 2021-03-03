from rest_framework.exceptions import ValidationError

from ..conf import conf

def get_error(error_message):
    ERROR = {
        'detail': '',
        'errors': [
            {
                "code": "0000",
                "field": None,
                "message": error_message
            }
        ]
    }

    return ERROR


class RestApiException(ValidationError):
    status_code = 400
    default_detail = ""


class SMSWaitException(RestApiException):
    default_detail = get_error(conf.SMS_WAIT_TIME)


class UserAlreadyExistException(RestApiException):
    default_detail = get_error(conf.SMS_USER_ALREADY_EXIST)

class SMSCodeNotFoundException(RestApiException):
    default_detail = get_error(conf.SMS_CODE_NOT_FOUND)