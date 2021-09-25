from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateDestroyAPIView

app_name = 'token_authentication'
urlpatterns = [
    path('user/', UserRetrieveUpdateDestroyAPIView.as_view()),
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
]
