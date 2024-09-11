from rest_framework import serializers

from hotels.models import HotelObject, Review, Service
from users.serializer import UserSerializer
from rooms.serializer import ImageSerializer, RoomSerializer


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = "__all__"


class ServicesSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = "__all__"


class HotelSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)
    services = ServicesSerializer(many=True, read_only=True)

    class Meta:
        model = HotelObject
        fields = "__all__"
