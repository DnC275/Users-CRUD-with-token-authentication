from django.urls import path

from .views import RegistrationAPIView, LoginAPIView, UserRetrieveUpdateDestroyAPIView, AllUsersView

app_name = 'token_authentication'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    path('users/all/', AllUsersView.as_view({'get': 'list'})),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view()),
]
