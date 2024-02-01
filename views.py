from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    context={
        "variable":"this is used to send the variable to the index html file",
        "variable1":"another teseting"
    }
    return render(request,'index.html',context)



def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        # phone=request.POST.get('phone')
        # contacts = Contact.objects.all() 
        new_contact=Contact(name=name,email=email,date=datetime.today())
        new_contact.save() 
        messages.success(request, "Your details has been saved!")
    return render(request,'contact.html')