from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from client.forms import PaymetForm
from client.models import PaymentSubmission, RequestReservations

from everything.models import RoomRegestration, ClientRegistration, BookingForm
from .forms import ClientRegistrationForm, DashForm, ReservationForm
from django.contrib.auth.decorators import login_required
# Create your views here.



def LoginPage1(request):
    page = 'LoginPage'

    if request.user.is_authenticated:
        return redirect('DashbordPage')
    if request.method=="POST":
        userName = request.POST.get('username').lower()
        passWord = request.POST.get('Password')

        user = authenticate(request, username=userName, password=passWord)

        if user is not None:
            login(request, user)
            return redirect('DashbordPage')
        else:
            messages.error(request, 'User name or password doesn\'t exist')

    context = {'page': page}
    return render(request, 'everything/loginPage.html', context)


def logoutPage(request):
    logout(request)
    return redirect('HomePage')


def RegisterPage(request):
    form = UserCreationForm()

    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('HomePage') 
        else:
            messages.error(request, 'An error occured during registeration')

    return render(request, 'everything/loginPage.html', {'form':form})


def HomePage(request):
    return render(request,'everything/home.html')

#dashbords

@login_required(login_url='LoginPage')
def DashBord(request):
    client = ClientRegistration.objects.all()
    room = RoomRegestration.objects.all()
    reserve = BookingForm.objects.all()
    stutes = RequestReservations.objects.all()
    quations = PaymentSubmission.objects.all()
            
    context = {'room':room, "client":client, 'reserve':reserve, 'statues':stutes, "quation":quations}
    return render(request, 'everything/Dashbord.html', context)


@login_required(login_url='LoginPage')
def DashbordTablePageClient(request):
    form = ClientRegistration.objects.all()

    quation = PaymentSubmission.objects.all()
    stutes = RequestReservations.objects.all()
    context = {'form': form, 'statues':stutes, "quation":quation}

    return render(request, 'everything/DashBordTabel-Client.html', context)


@login_required(login_url='LoginPage')
def DashbordTablePageRoom(request):
    form = RoomRegestration.objects.all()
    stutes = RequestReservations.objects.all()
    quations = PaymentSubmission.objects.all()
    context = {'form': form, 'statues':stutes, "quation":quations}

    return render(request, 'everything/DashBordTabel-Room.html', context)


@login_required(login_url='LoginPage')
def DashbordTablePageReservation(request):
    form = BookingForm.objects.all()
    stutes = RequestReservations.objects.all()
    quations = PaymentSubmission.objects.all()
    context = {"form":form, 'statues':stutes, "quation":quations}
    return render(request, 'everything/DashBordTabel-Reservation.html', context)


@login_required(login_url='LoginPage')
def RoomCreatePage(request):
    form = DashForm()
    room = RoomRegestration.objects.all()
    stutes = RequestReservations.objects.all()
    quations = PaymentSubmission.objects.all()
    if request.method == "POST":
        form = DashForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('DashbordTablePage')


    context = {'form' : form, "room": room, 'statues':stutes, "quation":quations}
    return render(request, 'everything/RoomCreation.html', context)


@login_required(login_url='LoginPage')
def RoomUpdatePage(request, pk):
    room = RoomRegestration.objects.get(id=pk)
    form = DashForm(instance=room)
    stutes = RequestReservations.objects.all()
    quations = PaymentSubmission.objects.all()
    if request.method == "POST":
        form = DashForm(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save()
            return redirect('DashbordTablePage')


    context = {'form': form ,"room": room, 'statues':stutes, "quation":quations}
    return render(request, 'everything/RoomCreation.html', context)


@login_required(login_url='LoginPage')
def ClientRegisterationPage(request):
    unavaliable_room = []
    reserved_rom = []
    form = ClientRegistrationForm()
    RoomS = RoomRegestration.objects.all()
    client = ClientRegistration.objects.all()
    stutes = RequestReservations.objects.all()
    quations = PaymentSubmission.objects.all()
    all_reserve = BookingForm.objects.all()

    for room in RoomS:
        for custumer in client:
            if custumer.Room_Been_Registered == room:
                rooms = room.Room_Name
                unavaliable_room.append(rooms)


    for room in RoomS:
        for reserv in all_reserve:
            if reserv.Room_Number == room:
                reserved_rom.append(room.Room_Name)


    if request.method == "POST":
        form= ClientRegistrationForm(request.POST)

        payment_method = request.POST.get('Payment_Status')

        room_Room_Been_Registered = request.POST.get('Room_Been_Registered')
        Idd = RoomRegestration.objects.get(Room_Name=room_Room_Been_Registered)


        ClientRegistration.objects.create(
        Client_Name = request.POST.get('Client_Name'),
        Password_assigned = request.POST.get('Password_assigned'),
        Phone_Number = request.POST.get('Phone_Number'),
        Date_of_Registration = request.POST.get('Date_of_Registration'),
        Client_Address = request.POST.get('Client_Address'),
        Tin_Number = request.POST.get('Tin_Number'),
        Email = request.POST.get('Email'),
        Payment_Status = payment_method,
        Room_Been_Registered = Idd 
        )
        return redirect("DashbordTablePageClient")

    context = {"form":form , "rooms":RoomS, 'client':client, 
    'unavaliable_room':unavaliable_room,"reserved_rom":reserved_rom,
    'statues':stutes, "quation":quations,
    } 
    return render(request, 'everything/ClientRegistration.html', context)


@login_required(login_url='LoginPage')
def ClientUpdatePage(request, pk):
    room = ClientRegistration.objects.get(id=pk)
    form = ClientRegistrationForm(instance=room)
    RoomS = RoomRegestration.objects.all()
    client = ClientRegistration.objects.all()
    all_reserve = BookingForm.objects.all()
    stutes = RequestReservations.objects.all()
    quations = PaymentSubmission.objects.all()

    reserved_rom = []
    unavaliable_room=[]
    for roo in RoomS:
        for custumer in client:
            if custumer.Room_Been_Registered == roo:
                rooms = roo.Room_Name
                unavaliable_room.append(rooms)

    for roo in RoomS:
        for reserv in all_reserve:
            if reserv.Room_Number == roo:
                reserved_rom.append(roo.Room_Name)



    unavaliable_room.remove(room.Room_Been_Registered.Room_Name)


    if request.method == 'POST':
        form = ClientRegistrationForm(request.POST, instance=room)

        payment_method = request.POST.get('Payment_Status')

        room_Room_Been_Registered = request.POST.get('Room_Been_Registered')
        Idd = RoomRegestration.objects.get(Room_Name=room_Room_Been_Registered)

        room.Client_Name = request.POST.get('Client_Name')
        room.Password_assigned = request.POST.get('Password_assigned')
        room.Phone_Number = int(request.POST.get('Phone_Number'))
        room.Date_of_Registration = request.POST.get('Date_of_Registration')
        room.Client_Address = request.POST.get('Client_Address')
        room.Tin_Number = request.POST.get('Tin_Number')
        room.Email = request.POST.get('Email')
        room.Room_Been_Registered = Idd
        room.Payment_Status = payment_method
        room.save()

        
        return redirect("DashbordTablePageClient")
    context = {"form":form, "rooms":RoomS, "room": room, "unavaliable_room":unavaliable_room, "reserved_rom":reserved_rom,
    'statues':stutes, "quation":quations,
    }
    return render(request, 'everything/ClientRegistration.html', context)



@login_required(login_url='LoginPage')
def ClientDeletePage(request, pk):
    room = ClientRegistration.objects.get(id=pk)
    stutes = RequestReservations.objects.all()
    quations = PaymentSubmission.objects.all()
    if request.method == 'POST':
        room.delete()
        return redirect('DashbordTablePageClient')

    return render(request, 'everything/delete-files.html', {'obj':room, 'statues':stutes, "quation":quations})

    

@login_required(login_url='LoginPage')
def ViewRoom(request):
    room = RoomRegestration.objects.all()
    stutes = RequestReservations.objects.all()
    quations = PaymentSubmission.objects.all()
    return render(request, 'everything/view-room-photo.html', {'room':room, 'statues':stutes, "quation":quations})


@login_required(login_url='LoginPage')
def DeleteFunction(request, pk):
    room = RoomRegestration.objects.get(id=pk)
    stutes = RequestReservations.objects.all()
    quations = PaymentSubmission.objects.all()

    if request.method == 'POST':
        room.delete()
        return redirect('DashbordTablePage')

    return render(request, 'everything/delete-files.html', {'obj':room, 'statues':stutes, "quation":quations})


@login_required(login_url='LoginPage')
def ReservationCreation(request):
    form = ReservationForm()
    rooms = RoomRegestration.objects.all()
    client = ClientRegistration.objects.all()
    stutes = RequestReservations.objects.all()
    quations = PaymentSubmission.objects.all()
    unavaliable_room = []


    for room in rooms:
        for custumer in client:
            if custumer.Room_Been_Registered == room:
                unavaliable_room.append(room.Room_Name)

    if request.method =="POST":
        form = ReservationForm(request.POST)

        Room_Number = request.POST.get('Room_Number')
        Idd = RoomRegestration.objects.get(Room_Name=Room_Number)

        BookingForm.objects.create(
        Customer_Name = request.POST.get('Customer_Name'),
        Email = request.POST.get('Email'),
        Phone_Number = request.POST.get('Phone_Number'),
        Client_Address = request.POST.get('Client_Address'),
        Date_of_Registration = request.POST.get('Date_of_Registration'),

        Advance_payed = request.POST.get('Advance_payed'),
        Tin_Number = request.POST.get('Tin_Number'),
        Payment_Method = request.POST.get('Payment_Method'),
        Room_Number = Idd,


        Agrement_Starting_Date = request.POST.get('Agrement_Starting_Date'),
        Agrement_Ending_Date = request.POST.get('Agrement_Ending_Date'),
        Begining_Day = request.POST.get('Begining_Day'),
        Ending_Day = request.POST.get('Ending_Day'),
        )
        return redirect("DashbordTablePageReservation")


    context={"form":form, "rooms":rooms, "client":client, "unavaliable_room":unavaliable_room,
    'statues':stutes, "quation":quations
    }

    return render(request, 'everything/reservation-edit.html', context)


@login_required(login_url='LoginPage')
def ReservationUpdate(request, pk):
    reservation = BookingForm.objects.get(id=pk)
    form= ReservationForm(instance=reservation)
    rooms = RoomRegestration.objects.all()
    client = ClientRegistration.objects.all()
    all_reserve = BookingForm.objects.all()
    stutes = RequestReservations.objects.all()
    quations = PaymentSubmission.objects.all()
    
    unavaliable_room = []
    reserved_rom = []


    for room in rooms:
        for custumer in client:
            for reserv in all_reserve:
                if (custumer.Room_Been_Registered == room ):
                    unavaliable_room.append(room.Room_Name)

    for room in rooms:
        for reserv in all_reserve:
            if reserv.Room_Number == room:
                reserved_rom.append(room.Room_Name)

    reserved_rom.remove(reservation.Room_Number.Room_Name)

    if request.method == "POST":
        form = ReservationForm(request.POST, instance=reservation)
        Room_Number = request.POST.get('Room_Number')
        Idd = RoomRegestration.objects.get(Room_Name=Room_Number)

        reservation.Customer_Name = request.POST.get('Customer_Name')
        reservation.Email = request.POST.get('Email')
        reservation.Phone_Number = request.POST.get('Phone_Number')
        reservation.Client_Address = request.POST.get('Client_Address')
        reservation.Date_of_Registration = request.POST.get('Date_of_Registration')

        reservation.Advance_payed = request.POST.get('Advance_payed')
        reservation.Tin_Number = request.POST.get('Tin_Number')
        reservation.Payment_Method = request.POST.get('Payment_Method')
        reservation.Room_Number = Idd

        reservation.Agrement_Starting_Date = request.POST.get('Agrement_Starting_Date')
        reservation.Agrement_Ending_Date = request.POST.get('Agrement_Ending_Date')
        reservation.Begining_Day = request.POST.get('Begining_Day')
        reservation.Ending_Day = request.POST.get('Ending_Day')
        reservation.save()


        return redirect('DashbordTablePageReservation')


    context={'form':form, 'reservation':reservation, 'rooms':rooms, 'client':client, 'unavaliable_room':unavaliable_room,
    'statues':stutes, "quation":quations
    }
    return render(request, 'everything/reservation-edit.html', context)


@login_required(login_url='LoginPage')
def DeleteResrvaton(request, pk):
    reservation = BookingForm.objects.get(id=pk)
    stutes = RequestReservations.objects.all()
    quations = PaymentSubmission.objects.all()

    if request.method == 'POST':
        reservation.delete()
        return redirect('DashbordTablePageClient')

    return render(request, 'everything/delete-files.html', {'obj':reservation, 'statues':stutes, "quation":quations})



@login_required(login_url='LoginPage')
def RoomStatic(request):
    room = RoomRegestration.objects.all()
    client = ClientRegistration.objects.all()
    reservation = BookingForm.objects.all()
    stutes = RequestReservations.objects.all()
    quations = PaymentSubmission.objects.all()
    reserved_room = []
    free_room = []
    for ROOms in room:
        for customer in reservation:
            if customer.Room_Number == ROOms:
                reserved_room.append(ROOms.Room_Name)


    for ROOms in room:
        for customer in client:
            if customer.Room_Been_Registered == ROOms:
                free_room.append(ROOms.Room_Name)

    
    context ={'room':room, 'client':client  ,'reservation':reservation, "reserved_room":reserved_room, "free_room":free_room, 
    'statues':stutes, "quation":quations
    }
    return render(request, 'everything/room-static.html', context)


@login_required(login_url='LoginPage')
def SeeStatic(request, pk):
    stutes = RequestReservations.objects.all()
    quations = PaymentSubmission.objects.all()
    client = ClientRegistration.objects.get(id=pk)
    time = client.Date_of_Registration
    time = datetime.now().date() - time 
    time = time.days
    many=client.Room_Been_Registered.Room_costes/30
    total = time*many

    context = {'client':client,'total':total, 'statues':stutes, "quation":quations}
    return render(request, 'everything/see-room-status.html', context)


@login_required(login_url='LoginPage')
def InboxPayment(request):
    quations = PaymentSubmission.objects.all()
    Rservation = RequestReservations.objects.all()
    context={"notification":quations, "requests":Rservation}
    return render(request,'everything/inboxPayment.html', context)


@login_required(login_url='LoginPage')
def seePayment(request, pk):
    request_customre = PaymentSubmission.objects.get(id=pk)
    context = {"request":request_customre}
    return render(request, 'everything/seePayment-customerrequest.html', context)


def seeReserve(request, pk):
    resrev_See = RequestReservations.objects.get(id=pk)
    context = {"Resrvation":resrev_See}
    return render(request, "everything/see-resrvation-request.html", context)


@login_required(login_url='LoginPage')
def DeletePaymentRequest(request, pk):
    Payment_check = PaymentSubmission.objects.get(id=pk)
    if request.method == 'POST':
        Payment_check.delete()
        return redirect("DashbordPage")

    return render(request, 'everything/delete-files.html', {"obj":Payment_check})


@login_required(login_url='LoginPage')
def DeleteResevationRequest(request, pk):
    Reservation_check = RequestReservations.objects.get(id=pk)
    if request.method == 'POST':
        Reservation_check.delete()
        return redirect("DashbordPage")

    return render(request, 'everything/delete-files.html', {"obj":Reservation_check})