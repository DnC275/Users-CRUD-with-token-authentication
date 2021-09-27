from .permissions import UsersObservationPermission
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import LoginSerializer, RegistrationSerializer, UserSerializer, AdminUserSerializer
from .models import User


class RegistrationView(CreateModelMixin, GenericViewSet):
    permission_classes = (IsAdminUser,)
    serializer_class = RegistrationSerializer


class LoginAPIView(RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated, UsersObservationPermission,)
    serializer_class = UserSerializer

    def get_serializer_class(self):
        return AdminUserSerializer if self.request.user.is_staff else UserSerializer


class AllUsersView(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        return AdminUserSerializer if self.request.user.is_staff else UserSerializer
