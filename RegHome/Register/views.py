from django.shortcuts import render
from Register.models import *
# Create your views here.
def GetStudReg(request):
    return render(request,'Register/Registration.html')


def GetLogin(request):
    return render(request,'Register/Login.html')

def GetHome(request):
    queryset=Register.objects.all()
    context={
        "object_list":queryset
    }
    return render(request, 'Register/Home2.html', context)

def GetStudVal(request):
    fname = request.POST.get("fname")
    lname=request.POST.get("lname")
    age=request.POST.get("age")
    uname=request.POST.get("uname")
    pwd = request.POST.get("pwd")
    cpwd = request.POST.get("cpwd")

    ob=Register(fname=fname,lname=lname,age=age,uname=uname,pwd=pwd,cpwd=cpwd)
    ob.save()

    context={}
    data=Register.objects.all()
    context['data']=data


    return render(request,'Register/Home.html',context)