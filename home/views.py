from django.shortcuts import render,HttpResponse
from datetime import datetime as dt
from home.models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    context={

        "variable":"sobi is great",
        "age":28

    }
    # messages.success(request,"hello sobi")
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def services(request):
    return render(request,"services.html")


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phone=phone,desc=desc,date=dt.today())
        contact.save()
        messages.success(request, "Your message has been sent.Thankyou for contact us")
    return render(request,"contact.html")





