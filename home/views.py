
from pyexpat.errors import messages
from django.shortcuts import render,redirect
from datetime import datetime
from django.contrib.auth.models import User
from home.models import Contact, UaeTicket, hotels, Signup
# Create your views here.
def index(request):
    return render(request,'index.html')
    

def Pakistanhotels(request):
     return render(request,'Pakistanhotels.html')
def Uaehotels(request):
    return render(request,'Uaehotels.html')
def Otherhotels(request):
    return render(request,'Otherhotels.html')

def Others(request):
    return render(request,'Others.html')
    
def Uae(request):
    return render(request,'Uae.html')
    
def Pakistan(request):
    return render(request,'Pakistan.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        em = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        em.save()
    return render(request,'contact.html')
    
def services(request):
   return render(request,'services.html')

def ticket(request):
   return render(request,'ticket.html')

def info(request):
   return render(request,'info.html')
def attabad(request):
   return render(request,'attabad.html')
def naran(request):
   return render(request,'naran.html')
def info2(request):
   return render(request,'info2.html')
def uaeticket(request):
    
     if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        cnic = request.POST.get('cnic')
        passport = request.POST.get('passport')
        payment = request.POST.get('payment')
        account = request.POST.get('account')
        place = request.POST.get('place')
        image = request.POST.get('image')
        uaeticket= UaeTicket( payment=payment, name=name, email=email, image=image, cnic=cnic, passport=passport, account=account, place=place, date = datetime.today())
        uaeticket.save()

     return render(request,'uaeticket.html')

def BookUae(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        account = request.POST.get('account')
        payment = request.POST.get('payment')
        em= hotels(name=name, email=email, account=account, payment=payment, date = datetime.today())
        em.save()
    return render(request,'BookUae.html')

def Signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(fname, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.password = pass2
        myuser.save()
        messages.success(request, "Your account has been successfully created")

    
  
     
      
    