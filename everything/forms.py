from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import ClientRegistration, RoomRegestration, BookingForm


class DashForm(ModelForm):
    class Meta:
        model = RoomRegestration
        fields = '__all__'



class ClientRegistrationForm(ModelForm):
    class Meta:
        model = ClientRegistration
        fields = "__all__"




class ReservationForm(ModelForm):
    class Meta:
        model=BookingForm
        fields = "__all__"

