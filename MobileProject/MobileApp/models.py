from django.db import models
from datetime import datetime,date

# Create your models here.
class users(models.Model):
    name=models.CharField(max_length=200)
    address=models.CharField(max_length=500)
    mobilenum=models.IntegerField()
    emailid=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    isActive=models.BooleanField(default=True)

    def __str__(self):
        return self.name

class color(models.Model):
    colorname=models.CharField(max_length=200)

    def __str__(self):
        return self.colorname

class category(models.Model):
    category_name=models.CharField(max_length=200)

    def __str__(self):
        return self.categoryname

class brand(models.Model):
    brand_name=models.CharField(max_length=200)

    def __str__(self):
        return self.brand_name

class Product(models.Model):
    product_quantity=models.IntegerField()
    product_name=models.CharField(max_length=200)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    price=models.IntegerField()
    ram=models.CharField(max_length=100)
    frontcam=models.CharField(max_length=100)
    rearcam=models.CharField(max_length=200)
    color=models.ForeignKey(color,on_delete=models.CASCADE)
    product_code=models.CharField(max_length=100)
    brand=models.ForeignKey(brand,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(users,on_delete=models.CASCADE)
    # date=models.DateField(default=datetime.now)
    date=models.DateField(auto_now_add=True)
