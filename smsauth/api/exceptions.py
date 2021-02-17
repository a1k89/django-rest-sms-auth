from rest_framework.exceptions import ValidationError


class RestApiException(ValidationError):
    status_code = 400
    default_detail = ""
