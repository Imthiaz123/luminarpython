from django.shortcuts import render,redirect
from MobileApp.forms import *
from MobileApp.models import *

# Create your views here.

def usercreate(request):

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listuser')

    form = UserForm()
    return render(request, "Registration/Registration.html", {"form": form})

def listuser(request):
    qs=users.objects.all()
    context={}
    context["data"]=qs
    return render(request,"Registration/ListUser.html",context)

def userlogin(request):
    form = LoginForm()
    return render(request, "Registration/Login.html", {"form": form})