from django.db import models

# Create your models here.
class category(models.Model):
    categoryname=models.CharField(max_length=200)

    def __str__(self):
        return self.categoryname

class product(models.Model):
    productname=models.CharField(max_length=200)
    productcategory=models.ForeignKey(category,on_delete=models.CASCADE)
    price=models.IntegerField()
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.productname
