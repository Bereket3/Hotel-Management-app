from rest_framework.generics import ListAPIView, CreateAPIView

from rooms.models import RoomsObject
from rooms.serializer import RoomSerializer


class ListCreateRoomsAPIViews(ListAPIView, CreateAPIView):
    serializer_class = RoomSerializer
    queryset = RoomsObject.objects.all()
