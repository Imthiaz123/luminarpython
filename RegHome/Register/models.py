from django.db import models

# Create your models here.
class Register(models.Model):
    fname=models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    age=models.IntegerField()
    uname = models.CharField(max_length=200)
    pwd = models.CharField(max_length=200)
    cpwd = models.CharField(max_length=200)


    def __str_(self):
        return (self.fname)