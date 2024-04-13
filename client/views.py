from django.shortcuts import render, redirect
from client.models import PaymentSubmission, RequestReservations
from django.contrib import messages
from datetime import datetime
from everything.models import ClientRegistration, RoomRegestration
from client.forms import PaymetForm, ReservationForm
from django.core.files.storage import FileSystemStorage

def CustumerLoginPage(request):
    page = 'CustumerLoginPage'

    if request.method == "POST":
        adminName = request.POST.get('Admin_Name')
        client = request.POST.get('username')
        passWord = request.POST.get('password')
        try:
            password = ClientRegistration.objects.get(Password_assigned=passWord)
            name = ClientRegistration.objects.get(Client_Name=client)
            if all([password, name])  is not None:
                client_id = ClientRegistration.objects.filter(Client_Name=client)
                return redirect("HomePage1")
            else:
                messages.error(request, "you must have enterd somthing wrong")
        except:
            messages.error(request, "you must have enterd somthing wrong")

        


    context ={'Page':page}
    return render(request, "everything/loginPage.html", context)


def HomePage(request):
    Client = ClientRegistration.objects.all()
    context={"client":Client}
    return render(request, 'client/HomePage.html', context)


def SendPayment(request):
    form = PaymetForm()
    rooms = RoomRegestration.objects.all()
    client = ClientRegistration.objects.all()
    if request.method == "POST" and request.FILES['Photo_Bill']:
        form = PaymetForm(request.POST, request.FILES)
        upload = request.FILES['Photo_Bill']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)

        customer = request.POST.get("Client_name")
        Idd = ClientRegistration.objects.get(Client_Name=customer)
        
        Room_Registered = request.POST.get("Room_ID")
        Room = RoomRegestration.objects.get(Room_Name=Room_Registered)

        PaymentSubmission.objects.create(
        Client_name = Idd,
        Room_ID = Room,
        Photo_Bill = upload,
        )
        messages.success(request, 'Your Request has been sent successfully')
            

    context = {"form":form, "rooms":rooms, "client":client, 'file_url':file_url}
    return render(request, 'client/sendRequest.html', context)


def RequestReservation(request):
    form = ReservationForm()
    room = RoomRegestration.objects.all()
    client = ClientRegistration.objects.all()
    unavliable_room = []
    for ROOm in room:
        for customer in client:
            if customer.Room_Been_Registered == ROOm:
                unavliable_room.append(ROOm.Room_Name)

    if request.method == "POST":
        form = ReservationForm(request.POST)
        Room_Registered = request.POST.get("Room_ID")
        Room = RoomRegestration.objects.get(Room_Name=Room_Registered)
        RequestReservations.objects.create(
            Client_name = request.POST.get("Client_name"),
            Client_phone = request.POST.get("Client_phone"),
            Room_ID=Room,
            Date_beging = request.POST.get("Date_beging"),
            Date_ending = request.POST.get("Date_ending")
        )

        messages.success(request, 'Your request have benn successfully submitted')
    context={"unavliable_room":unavliable_room, "rooms":room}

    return render(request, 'client/reservation-request.html', context)


def ViewDetal(request, pk):
    client = ClientRegistration.objects.get(id=pk)
    time=client.Date_of_Registration
    time = datetime.now().date() - time 
    mony = client.Room_Been_Registered.Room_costes/30
    total = time.days*mony


    context={'client': client, "total":total}
    return render(request, 'client/View-detail.html', context)