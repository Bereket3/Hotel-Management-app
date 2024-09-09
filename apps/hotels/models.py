from django.db import models

from rooms.models import Images, RoomsObject
from users.models import AuthUserModel


class Review(models.Model):
    reviewer = models.ForeignKey(AuthUserModel, on_delete=models.CASCADE)
    review = models.TextField()
    stars = models.FloatField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reviewer.__str__()


class Services(models.Model):
    name = models.CharField(max_length=200)
    image = models.ManyToManyField(Images)
    description = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.__str__()


class HotelOject(models.Model):
    name = models.CharField(max_length=200)
    hotel_owner = models.ForeignKey(
        AuthUserModel, on_delete=models.CASCADE, related_name="owned_hotels"
    )
    services = models.ManyToManyField(Services)
    rooms = models.ManyToManyField(RoomsObject)
    review_object = models.ManyToManyField(Review)
    hotel_staff = models.ManyToManyField(AuthUserModel, related_name="staff_hotels")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name.__str__()
