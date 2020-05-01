from django.shortcuts import render,redirect
from ProductApp.models import category,product
from ProductApp.forms import ProductForm,CategoryForm
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class CreateCategory(TemplateView):
    model_name=category
    form_class=CategoryForm
    template_name = "products/CreateCategory.html"

    def get(self, request, *args, **kwargs):
        context = {}
        context["catform"] = self.form_class
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("category_list")

class ListCategory(TemplateView):
    model_name = category
    template_name = "products/ListCategory.html"

    def get_querSet(self):
        return self.model_name.objects.all()

    def get(self, request, *args, **kwargs):
        context={}
        context["catlist"]=self.get_querSet()
        return render(request,self.template_name,context)

class CreateProduct(TemplateView):
    model_name=product
    form_class=ProductForm
    template_name = "products/CreateProduct.html"

    def get(self, request, *args, **kwargs):
        context={}
        context["form"]=self.form_class
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("product_list")

class ListProduct(TemplateView):
    model_name = product
    template_name = "products/ListProduct.html"

    def get_querSet(self):
        return self.model_name.objects.all()

    def get(self, request, *args, **kwargs):
        context={}
        context["list"]=self.get_querSet()
        return render(request,self.template_name,context)


class UpdateProduct(TemplateView):
    model_name=product
    form_class=ProductForm
    template_name = "products/EditProduct.html"

    def get_QuerySet(self):
        return self.model_name.objects.get(id=self.kwargs.get("pk"))

    def get(self, request, *args, **kwargs):
        form=self.form_class(instance=self.get_QuerySet())
        context={}
        context["form"]=form
        return render(request,self.template_name,context)

    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST,request.FILES)
        if form.is_valid():
            ob=self.get_QuerySet()
            ob.productname=form.cleaned_data["productname"]
            ob.productcategory=form.cleaned_data["productcategory"]
            ob.price=form.cleaned_data["price"]
            ob.image=form.cleaned_data["image"]
            ob.save()
            return redirect("product_list")
        else:
            context = {}
            context["form"] = form
            return render(request, self.template_name, context)

class ProductDel(TemplateView):
    model_name = product
    template_name = "products/DeleteProduct.html"
    form_class = ProductForm

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
            return redirect("product_list")



class ProductView(TemplateView):
    model_name = product
    template_name = "products/ViewProduct.html"

    def get_Queryset(self):
            return self.model_name.objects.get(id=self.kwargs.get('pk'))

    def get(self, request, *args, **kwargs):
            context = {}
            context["views"] = self.get_Queryset()
            return render(request, self.template_name, context)

class CategoryDel(TemplateView):
    model_name = category
    template_name = "products/CategoryDelete.html"
    form_class = CategoryForm

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
            return redirect("category_list")





# class ProductList(ListView):
#     model=product
#     template_name = "products/ListProduct.html"
#
#
# class ProductView(DetailView):
#     model = product
#     context_object_name = "obj"
#     template_name = "products/ViewProduct.html"
#
# class ProductCreate(CreateView):
#     model = product
#     fields=['productname','productcategory','price','image']
#     success_url = reverse_lazy('product_list')
#     template_name = "products/CreateProduct.html"
#
# class ProductUpdate(UpdateView):
#     model = product
#     fields = ['productname', 'productcategory', 'price', 'image']
#     template_name = "products/CreateProduct.html"
#     success_url = reverse_lazy('product_list')
#
# class ProductDelete(DeleteView):
#     model = product
#     success_url = reverse_lazy('product_list')
#     template_name = "products/product_confirm_delete.html"
#     context_object_name = "obj"







# def prodcreate(request):
#
#     if request.method=="POST":
#         form=ProductForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("listproduct")
#         else:
#             return render(request, "products/CreateProduct.html", {"form": form})
#
#     form=ProductForm()
#     return render(request,"products/CreateProduct.html",{"form":form})
#
# def listproduct(request):
#     qs=product.objects.all()
#     context={}
#     context["data"]=qs
#     return render(request,"products/ListProduct.html",context)
#
# def editproduct(request,pk):
#     qs = product.objects.get(pk=pk)
#     if request.method=="POST":
#         qs.delete()
#         form=ProductForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("listproduct")
#
#     form=ProductForm(instance=qs)
#     return render(request,"products/EditProduct.html",{"form":form})
#
# def viewproduct(request,pk):
#     qs=product.objects.get(pk=pk)
#     return render(request, "products/ViewProduct.html", {"qs": qs})
#
# def deleteproduct(request,pk):
#     qs = product.objects.get(pk=pk)
#     qs.delete()
#     return redirect("listproduct")