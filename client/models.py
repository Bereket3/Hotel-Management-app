from django.db import models

from everything.models import ClientRegistration, RoomRegestration

# Create your models here.
class PaymentSubmission(models.Model):
    Client_name = models.ForeignKey(ClientRegistration, on_delete=models.SET_NULL, null=True)
    Room_ID = models.ForeignKey(RoomRegestration, on_delete=models.SET_NULL, null=True)
    Photo_Bill = models.ImageField(upload_to="everything/statics/Photos/3")
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Client_name.Client_Name




class RequestReservations(models.Model):
    Client_name= models.CharField(max_length=50)
    Client_phone = models.IntegerField()
    Room_ID=models.ForeignKey(RoomRegestration, on_delete=models.SET_NULL,null=True)
    Date_beging = models.DateField()
    Date_ending=models.DateField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Client_name
