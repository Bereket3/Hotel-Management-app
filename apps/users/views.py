from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    ListAPIView,
    UpdateAPIView,
)
from .serializer import UserSerializer, RegisterSerializer
from .models import AuthUserModel


class CreateUserAPIView(CreateAPIView):
    queryset = AuthUserModel
    serializer_class = RegisterSerializer


class UpdateAndGetUserAPIView(UpdateAPIView, RetrieveAPIView):
    queryset = AuthUserModel
    serializer_class = UserSerializer
    lookup_field = "id"


class ListUserAPIView(ListAPIView):
    queryset = AuthUserModel.objects.all()
    serializer_class = UserSerializer
