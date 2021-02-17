from django.urls import path

from .views import AuthAPIView, EntryAPIView

urlpatterns = [
    path("sign-in/", EntryAPIView.as_view()),
    path("auth/", AuthAPIView.as_view()),
]
