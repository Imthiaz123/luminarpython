"""Product URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ProductApp.views import *



urlpatterns = [
    path('create/', CreateProduct.as_view(), name="product_create"),
    path('', ListProduct.as_view(), name="product_list"),
    path('update/<int:pk>', UpdateProduct.as_view(), name="product_update"),
    path('delete/<int:pk>', ProductDel.as_view(), name="product_delete"),
    path('view/<int:pk>', ProductView.as_view(), name="product_view"),

    path('createCategory/', CreateCategory.as_view(), name="category_create"),
    path('Categorylist/', ListCategory.as_view(), name="category_list"),
    path('Categorydelete/<int:pk>', CategoryDel.as_view(), name="cat_delete"),

]

# urlpatterns = [
#     path('',views.ProductList.as_view(),name="product_list"),
#     path('view/<int:pk>', views.ProductView.as_view(),name="product_view"),
#     path('create/', views.ProductCreate.as_view(), name="product_create"),
#     path('update/<int:pk>', views.ProductUpdate.as_view(), name="product_update"),
#     path('delete/<int:pk>', views.ProductDelete.as_view(), name="product_delete"),
# ]

# urlpatterns = [
#     path('CreateProduct/',prodcreate,name="createproduct"),
#     path('ListProduct/',listproduct,name="listproduct"),
#     path('editProduct/<int:pk>',editproduct,name="Editproduct"),
#     path('viewProduct/<int:pk>', viewproduct, name="viewproduct"),
#     path('deleteProduct/<int:pk>', deleteproduct, name="deleteproduct"),
# ]
