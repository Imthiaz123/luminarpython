from django.forms import ModelForm
from ProductApp.models import category,product
from django.forms import ModelChoiceField


class ProductForm(ModelForm):
    class Meta:
        model=product
        fields=['productname','productcategory','price','image']


    def clean(self):

        cleaned_data=super().clean()
        name=cleaned_data.get("productname")
        category=cleaned_data.get("productcategory")
        price=cleaned_data.get("price")

        if price < 10:
            msg="please provide correct value for price"
            self.add_error("price",msg)


class CategoryForm(ModelForm):
    class Meta:
        model=category
        fields=['categoryname']