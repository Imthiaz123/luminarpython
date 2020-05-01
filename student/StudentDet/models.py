from django.db import models

# Create your models here.
class student(models.Model):
    roll=models.CharField(max_length=120)
    name=models.CharField(max_length=200)
    course=models.CharField(max_length=120)
    address=models.CharField(max_length=250)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.name