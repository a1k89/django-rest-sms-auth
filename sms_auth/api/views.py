from rest_framework import generics, permissions

from ..conf import conf
from ..services import AuthService, GeneratorService
from .mixins import ResponsesMixin
from .serializers import \
    AuthSerializer, \
    EntrySerializer, \
    ChangePhoneNumberSerializer


class EntryAPIView(ResponsesMixin, generics.GenericAPIView):
    """
    Single endpoint to sign-in/sign-up
    :param
        - phone_number
    """

    permission_classes = [
        permissions.AllowAny,
    ]

    serializer_class = EntrySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data.get("phone_number")
            GeneratorService.execute(phone_number=phone_number)
            return self.simple_text_response()
        else:
            return self.error_response(serializer.errors)


class AuthAPIView(ResponsesMixin, generics.GenericAPIView):
    """
    Single endpoint to auth thgrough phone_number + code
        params:
         - phone_number
         - code
    """

    permission_classes = [
        permissions.AllowAny,
    ]

    serializer_class = AuthSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data.get("phone_number")
            code = serializer.validated_data.get("code")
            user = AuthService.execute(phone_number=phone_number, code=code)
            success_value = getattr(user, conf.SMS_AUTH_SUCCESS_KEY)

            return self.success_objects_response(success_value)
        else:
            return self.error_response(serializer.errors)


class ChangePhoneNumberAPIView(ResponsesMixin, generics.GenericAPIView):
    serializer_class = ChangePhoneNumberSerializer

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            new_phone_number = serializer.validated_data.get('new_phone_number')
            owner = request.user
            GeneratorService.execute(phone_number=new_phone_number, owner=owner)

            return self.simple_text_response()

        else:
            return self.error_response(serializer.errors)
