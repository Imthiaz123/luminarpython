from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200)
    course=models.CharField(max_length=200)
    marks=models.IntegerField()
    rollnum=models.IntegerField(unique=True)

    def __str_(self):
        return (self.name)