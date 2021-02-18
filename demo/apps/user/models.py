from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    age = models.PositiveIntegerField(default=10)


    @property
    def jwt_token(self):
        return 'some-generated-auth-token'
