from django.urls import path

from .views import RegistrationView, LoginAPIView, UserRetrieveUpdateDestroyAPIView, AllUsersView

app_name = 'token_authentication'
urlpatterns = [
    path('users/', RegistrationView.as_view({'post': 'create'})),
    path('users/login/', LoginAPIView.as_view()),
    path('users/all/', AllUsersView.as_view({'get': 'list'})),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view()),
]
