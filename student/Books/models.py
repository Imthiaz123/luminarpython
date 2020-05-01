from django.db import models

# Create your models here.

class Book(models.Model):
    bookname=models.CharField(unique=True,max_length=200)
    category=models.CharField(max_length=200)
    price=models.IntegerField()
    pages=models.IntegerField()
    author=models.CharField(max_length=200)

    def __str__(self):
        return self.bookname