from .permissions import UsersObservationPermission
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from .renders import UserJSONRenderer
from .serializers import LoginSerializer, RegistrationSerializer, UserSerializer, AdminViewAllSerializer
from .models import User


class RegistrationView(CreateModelMixin, GenericViewSet):
    permission_classes = (IsAdminUser,)
    serializer_class = RegistrationSerializer


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, UsersObservationPermission,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(User.objects.get(pk=kwargs['pk']))
        self.check_object_permissions(request, serializer.instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})
        serializer = self.serializer_class(User.objects.get(pk=kwargs['pk']), data=serializer_data, partial=True)
        self.check_object_permissions(request, serializer.instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        serializer = self.serializer_class(User.objects.get(pk=kwargs['pk']))
        self.check_object_permissions(request, serializer.instance)
        instance = serializer.instance
        instance.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)


class AllUsersView(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        return AdminViewAllSerializer if self.request.user.is_staff else UserSerializer
