from django.shortcuts import render, redirect
from Books.forms import BookForm
from Books.models import Book
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class BookList(ListView):
    model=Book

class BookView(DetailView):
    model = Book
    context_object_name = "obj"
    template_name = "Books/book_view.html"

class BookCreate(CreateView):
    model = Book
    fields=['bookname','category','price','pages','author']
    success_url = reverse_lazy('book_list')
    template_name = "Books/BookCreate.html"

class BookUpdate(UpdateView):
    model = Book
    fields=['bookname','category','price','pages','author']
    success_url = reverse_lazy('book_list')
    template_name = "Books/BookCreate.html"

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')





# def bookcreate(request):
#
#     if request.method == "POST":
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("bookslist")
#
#     form = BookForm()
#     return render(request,"Books/BookCreate.html",{"form":form})
#
# def listbook(request):
#     queryset=Book.objects.all()
#     context={}
#     context["book"]=queryset
#     return render(request,"Books/BookList.html",context)
#
# def editbook(request,pk):
#     qs=Book.objects.get(pk=pk)
#     if request.method=="POST":
#         qs.delete()
#         form=BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect("bookslist")
#
#     form=BookForm(instance=qs)
#     return render(request,"Books/book_edit.html",{"form":form})
#
# def viewbook(request,pk):
#     qs=Book.objects.get(pk=pk)
#     return render(request, "Books/book_view.html", {"qs": qs})
#
# def delbook(request,pk):
#     qs = Book.objects.get(pk=pk)
#     qs.delete()
#     return redirect("bookslist")
