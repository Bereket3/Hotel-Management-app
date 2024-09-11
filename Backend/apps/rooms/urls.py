from django.urls import path

from rooms.views import ListCreateRoomsAPIViews


urlpatterns = [path("", ListCreateRoomsAPIViews.as_view(), name="list_rooms")]
