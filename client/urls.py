from django.urls import path, include
from client import views 
from system import settings
from django.conf.urls.static import static


urlpatterns = [
    #nessasary pages
    path('', views.HomePage, name='HomePage1'),
    path('Payment-submiton', views.SendPayment, name='SendPaymentPage'),
    path('request-reserveation', views.RequestReservation, name='RequestReservationPage'),
    path('view-detal/<int:pk>/', views.ViewDetal, name='ViewDetalPage'),
    #customers browsing
    path('Custumer-login/', views.CustumerLoginPage, name="CustumerLoginPage"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

