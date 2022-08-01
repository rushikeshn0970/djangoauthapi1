from django.urls import path, include
from account.views import UserRegistrationView
urlpatterns = [
    path(r'register/', UserRegistrationView.as_view(),
    name='register'),
]