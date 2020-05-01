from django.shortcuts import render, redirect
from BudgetApp.forms import *
from  django.views.generic import TemplateView
from django.utils.dateparse import parse_date
from django.db.models import Sum
from django.db.models.functions import TruncMonth,TruncWeek,TruncDay
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import logout

import matplotlib

class Home(TemplateView):


    template_name = "BudgetTemp/Home.html"

    def get(self, request, *args, **kwargs):
        user=request.session["username"]
        context={}
        context["user"]=user

        return render(request,self.template_name,context)

class Registration(TemplateView):

    form_class=RegisterForm
    model_name=users
    template_name = "BudgetTemp/registration.html"

    def get(self, request, *args, **kwargs):

        context={}
        context["form"]=self.form_class
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):

        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message":"created",'status':200})
            # return redirect("login_user")

class Login(TemplateView):

    form_class=LoginForm
    model_name=users
    template_name = "BudgetTemp/login.html"

    def get(self, request, *args, **kwargs):

        context={}
        context["form"]=self.form_class
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):

        form=self.form_class(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            qs=users.objects.get(username=username)

            print("query set",qs)

            if((qs.username==username) & (qs.password==password)):
                request.session["username"]=username
                return JsonResponse({"message":"login successfull",'status':200})
                # print("login username",username)
                #
                # return redirect("home")
            else:
                return JsonResponse({"message":"login failed",'status':204})



class CreateExpense(TemplateView):
    model_name=expense
    form_class=ExpenseForm
    template_name = "BudgetTemp/CreateExpense.html"

    def get(self, request, *args, **kwargs):
        # qs=self.model_name.objects.filter(user=request.session["username"])
        # print("query set",qs)
        user = request.session["username"]

        context={}
        context["form"]=self.form_class
        context["user"]=user
        # context["user"]=qs
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            user=request.session["username"]
            print("user:",user)
            category=form.cleaned_data["category"]
            expense_name = form.cleaned_data["expense_name"]
            amount = form.cleaned_data["amount"]
            date = form.cleaned_data["date"]
            obj=self.model_name(user=user,category=category,expense_name=expense_name,amount=amount,date=date)
            obj.save()
            return redirect("list_expense")
        else:
            context = {}
            context["form"] = self.form_class
            return render(request, self.template_name, context)



class ListExpense(TemplateView):

    model_name=expense
    template_name = "BudgetTemp/ListExpense.html"


    def get(self, request, *args, **kwargs):

        qs=self.model_name.objects.filter(user=request.session["username"])
        print("query set",qs)
        context={}

        user = request.session["username"]
        context["user"] = user

        context["list"]=qs
        return render(request,self.template_name,context)


class logout(TemplateView):
    def get(self, request, *args, **kwargs):
        del request.session["username"]
        return redirect('login_user')



class CalculateSumDate(TemplateView):
    model_name=expense
    form_class = dateInsertForm
    template_name = "BudgetTemp/ExpenseByDate.html"

    def get(self, request, *args, **kwargs):
        form=self.form_class
        context = {}
        user = request.session["username"]

        context["user"] = user
        context["form"] = form

        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = request.session["username"]
            from_date=form.cleaned_data["from_date"]
            to_date = form.cleaned_data["to_date"]
            print(from_date)
            print(to_date)
            qs=self.get_querySet(user,from_date,to_date)
            print("date query set",qs)
            context={}
            context['user']=user
            context['qs']=qs
            context['form']=form
            return render(request, self.template_name, context)


    def get_querySet(self, user, from_date, to_date):
        return self.model_name.objects.filter(user=user, date__gte=from_date, date__lte=to_date).values('category__category_name').annotate(categorysum=Sum('amount')).order_by('categorysum')



class CalculateSumCateg(TemplateView):
    model_name=expense
    form_class = CategoryInsertForm
    template_name = "BudgetTemp/ExpenseByCategory.html"

    def get(self, request, *args, **kwargs):
        form=self.form_class
        context = {}
        user = request.session["username"]

        context["user"] = user
        context["form"] = form

        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = request.session["username"]
            category_name = form.cleaned_data["category"]
            from_date=form.cleaned_data["from_date"]
            to_date = form.cleaned_data["to_date"]
            print(from_date)
            print(to_date)
            qs=self.get_querySet(user,category_name,from_date,to_date)
            print("date query set",qs)
            context={}
            context['user']=user
            context['qs']=qs
            context['form']=form
            return render(request, self.template_name, context)


    def get_querySet(self, user,category_name, from_date, to_date):
        return self.model_name.objects.filter(user=user, date__gte=from_date, date__lte=to_date,category__category_name=category_name).values('category__category_name').annotate(categorysum=Sum('amount')).order_by('categorysum')



