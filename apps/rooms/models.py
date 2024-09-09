from django.db import models


class Images(models.Model):
    image = models.ImageField(upload_to="pictures")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.__str__()


class RoomsObject(models.Model):
    room_id = models.CharField(max_length=400)
    number_of_people = models.IntegerField()
    images = models.ManyToManyField(Images)

    def __str__(self):
        return self.room_id.__str__()
