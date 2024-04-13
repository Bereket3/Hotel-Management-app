from datetime import datetime
from pickle import NONE
from random import choices
from secrets import choice
from django.db import models
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
import uuid

# Create your models here.
Payment_Method_choice = (('Every Month','Every Month'),('Every 3 month','Every 3 Month'),('Every 6 Month','Every 6 Month'), ('Every Year','Every Year'))

Payment_choice = (('have been payed','have been payed'),('is not payed','is not payed'))

Rent_status = (('is currently rented','is currently rented'),('is not rented yet','is not rented yet'))



class admin1(models.Model):
    admin = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    Admin_Email = models.EmailField()
    Bulding_Name = models.CharField(max_length=50)
    #photo_admin = models.ImageField(upload_to="everything/statics/Photos/3", default=None)
    Bulding_Location = models.CharField(max_length=50)
    Password_Admin = models.CharField(max_length=10, default="")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.admin.username)


class RoomRegestration(models.Model):
    Room_Name = models.CharField(max_length=50)
    Room_Type = models.CharField(max_length=50)
    Room_Catagory = models.CharField(max_length=50)
    Floor_No = models.CharField(max_length=100, default='')
    Remark = models.TextField(null=True, blank=True)
    Photo_Room = models.ImageField(upload_to='Photos/1', null=True, blank=True)
    Room_costes = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Room_Name





class ClientRegistration(models.Model):
    Client_Name = models.CharField(max_length=50)
    Phone_Number = models.IntegerField()
    Date_of_Registration = models.DateField()
    Client_Address = models.CharField(max_length=100)
    Tin_Number = models.IntegerField()
    Email = models.EmailField()
    #Photo_Client = models.ImageField(upload_to='')
    Room_Been_Registered = models.ForeignKey(RoomRegestration, on_delete=models.SET_NULL, null=True)
    Password_assigned = models.CharField(max_length=10, default="")
    Payment_Status = models.CharField(max_length=50, choices=Payment_choice, default='have been payed')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Client_Name


class BookingForm(models.Model):
    Customer_Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Client_Address = models.CharField(max_length=100)
    Phone_Number = models.IntegerField()
    Date_of_Registration = models.DateField()


    Advance_payed = models.IntegerField()
    Tin_Number = models.IntegerField()
    Room_Number = models.ForeignKey(RoomRegestration, on_delete=models.SET_NULL, null=True)
    Payment_Method = models.CharField(max_length=200, choices=Payment_Method_choice, null=True)

    Agrement_Starting_Date = models.DateField()
    Agrement_Ending_Date = models.DateField()

    Begining_Day = models.DateField()
    Ending_Day = models.DateField()
    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.Customer_Name

