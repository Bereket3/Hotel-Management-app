from rest_framework import serializers

from hotels.models import HotelOject, Review, Services


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelOject
        fields = ["__all__"]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["__all__"]


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ["__all__"]
