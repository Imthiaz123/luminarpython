from django.shortcuts import render
from student.models import Student
# Create your views here.
def GetStudPage(request):
    return render(request,'Student/StudHome.html')

def GetStudVal(request):
    id = request.POST.get("sid")
    fname=request.POST.get("name")
    course=request.POST.get("course")
    mark=request.POST.get("total")

    ob=Student(name=fname,course=course,marks=mark,rollnum=id)
    ob.save()

    context={}
    data=Student.objects.all()
    context['data']=data
    print(ob.name)

    return render(request,'Student/Output.html',context)