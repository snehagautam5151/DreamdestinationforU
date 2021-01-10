from django.shortcuts import render, HttpResponse 
from hello.models import Contact
from .forms import ContactCreate
from django.http import HttpResponse
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


# Create your views here.
def index(request):
       context = {
          "variable" : "this is context"
       }
       messages.success(request,"this is a text message")
       return render(request , "index.html",context )
def home(request):
   return render(request, "home.html")    


def about(request):
   return render(request , "about.html" )

def services(request):
   return render(request , "services.html" )
  
def contact(request):
       if request.method == "POST":
            name = request.POST.get('name')
            email = request.POST.get('email')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            state = request.POST.get('state')
            zip = request.POST.get('zip')
            contact = Contact (name= name, email=email, address=address, phone= phone,state= state, zip= zip)
            contact.save()
            messages.success(request, 'your message has been sent.')
       return render(request ,"contact.html")
 

