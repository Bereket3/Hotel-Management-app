from rest_framework import serializers

from rooms.models import Image, RoomsObject


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = "__all__"


class RoomSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = RoomsObject
        fields = "__all__"
