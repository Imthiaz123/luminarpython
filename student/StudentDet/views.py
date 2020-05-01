from django.shortcuts import render, redirect
from StudentDet.forms import studentCreationForm,StudentupdateForm
from StudentDet.models import student
from  django.views.generic import TemplateView

class CreateStudent(TemplateView):

    form_class=studentCreationForm
    model_name=student
    template_name = "StudentTemp/registration.html"

    def get(self, request, *args, **kwargs):

        context={}
        context["form"]=self.form_class
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):

        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")

class ListStudent(TemplateView):

    model_name=student
    template_name = "StudentTemp/ListStudent.html"

    def get_querySet(self):

        return self.model_name.objects.all()

    def get(self, request, *args, **kwargs):
        context={}
        context["stud"]=self.get_querySet()
        return render(request,self.template_name,context)

class UpdateStudent(TemplateView):
    model_name=student
    form_class=StudentupdateForm
    template_name = "StudentTemp/StudentEdit.html"

    def get_QuerySet(self):
        return self.model_name.objects.get(id=self.kwargs.get("pk"))

    def get(self, request, *args, **kwargs):
        form=self.form_class(instance=self.get_QuerySet())
        context={}
        context["form"]=form
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            ob=self.get_QuerySet()
            ob.name=form.cleaned_data["name"]
            ob.course=form.cleaned_data["course"]
            ob.address=form.cleaned_data["address"]
            ob.password=form.cleaned_data["password"]
            ob.save()
            return redirect("list")
        else:
            context = {}
            context["form"] = form
            return render(request, self.template_name, context)

class StudentDel(TemplateView):
    model_name=student
    template_name ="StudentTemp/DeleteStudent.html"
    form_class=StudentupdateForm

    def get_Queryset(self):
        return self.model_name.objects.get(id=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=self.get_Queryset())
        context = {}
        context["form"] = form
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        self.get_Queryset().delete()
        print("deleted")
        return redirect("list")

class StudentView(TemplateView):
    model_name=student
    template_name = "StudentTemp/StudentView.html"


    def get_Queryset(self):
        return self.model_name.objects.get(id=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
            context = {}
            context["view"] = self.get_Queryset-()
            return render(request, self.template_name, context)