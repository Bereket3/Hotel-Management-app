from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import ListUserAPIView, CreateUserAPIView, UpdateAndGetUserAPIView

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("token/refrash/", TokenRefreshView.as_view(), name="refrash"),
    path("create/", CreateUserAPIView.as_view(), name="create"),
    path("<str:id>/", UpdateAndGetUserAPIView.as_view(), name="update"),
    path("", ListUserAPIView.as_view(), name="get"),
]
