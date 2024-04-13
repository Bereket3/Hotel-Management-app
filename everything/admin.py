from django.contrib import admin
from .models import RoomRegestration, ClientRegistration,BookingForm, admin1
from client.models import PaymentSubmission, RequestReservations

# Register your models here.
admin.site.register(RoomRegestration)
admin.site.register(ClientRegistration)
admin.site.register(BookingForm)
admin.site.register(PaymentSubmission)
admin.site.register(RequestReservations)
admin.site.register(admin1)