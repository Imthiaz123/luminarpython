from django.forms import ModelForm
from Books.models import Book

class BookForm(ModelForm):
    class Meta:
        model=Book
        fields=['bookname','category','price','pages','author']