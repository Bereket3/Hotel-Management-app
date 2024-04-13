from django.urls import path, include
from . import views 
from system import settings
from django.conf.urls.static import static


urlpatterns = [
    #nessasary pages
    path('', views.HomePage, name='HomePage'),
    path('login/', views.LoginPage1, name='LoginPage'),
    path('register/', views.RegisterPage, name='register'),
    path('logout/', views.logoutPage, name="LogoutPage"),

    #Dashbords
    path('dashbord/', views.DashBord, name="DashbordPage"),
    path('DasbordTable-Room/', views.DashbordTablePageRoom, name="DashbordTablePage"),
    path('DasbordTable-Client/', views.DashbordTablePageClient, name="DashbordTablePageClient"),
    path('DasbordTable-Resrvation/', views.DashbordTablePageReservation, name="DashbordTablePageReservation"),


    #room creation and updates
    path('RoomForm/', views.RoomCreatePage, name="RoomCreationPage"),
    path('RoomUpdate/<int:pk>/', views.RoomUpdatePage, name="RoomUpdatePage"),


    #client creation and update
    path('ClientRegistration/', views.ClientRegisterationPage, name="ClientRegisterationPage"),
    path('ClientUpdate/<int:pk>/', views.ClientUpdatePage, name="ClientUpdatePage"),

    #reservation creation and delete
    path('make-reservation', views.ReservationCreation, name="ReservationCreationPage"),
    path('update-reservation/<int:pk>/', views.ReservationUpdate, name="ReservationUpdatePage"),

    #View and Delete paths
    path('view-room/', views.ViewRoom, name="ViewRoomPage"),
    path('delete-room/<int:pk>/', views.DeleteFunction, name="DeletePage"),
    path('delete-client/<int:pk>/', views.ClientDeletePage, name="ClientDeletePage"),
    path('delete-reservation/<int:pk>/', views.DeleteResrvaton, name="ReservationDeletePage"),


    #room static and others
    path('room-static/', views.RoomStatic, name="RoomStaticPage"),
    path('see-static/<int:pk>/', views.SeeStatic, name="SeeStaticPage"),


    #admin profile and stuff
    path('inbox/', views.InboxPayment, name='InboxRequestPage'),
    path('Payment-checking/<int:pk>', views.seePayment, name='PaymentCheckingPage'),
    path('Reservation-checking/<int:pk>', views.seeReserve, name='ReservtaionCheckingPage'),
    path('Delete-payment-Request/<int:pk>', views.DeletePaymentRequest, name='DeletePaymentRequestPage'),
    path('Delete-Reservation-Request/<int:pk>', views.DeleteResevationRequest, name='DeleteReservationRequestPage'),




] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


