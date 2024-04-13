from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from client.models import PaymentSubmission, RequestReservations


class PaymetForm(ModelForm):
    class Meta:
        model = PaymentSubmission
        fields ="__all__"



class ReservationForm(ModelForm):
    class Meta:
        model= RequestReservations
        fields ="__all__"