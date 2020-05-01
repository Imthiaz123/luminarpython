"""student URL Configuration

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
from .views import *
from Books import views

urlpatterns = [
    path('',views.BookList.as_view(),name="book_list"),
    path('view/<int:pk>', views.BookView.as_view(),name="book_view"),
    path('create/', views.BookCreate.as_view(),name="book_create"),
    path('update/<int:pk>', views.BookUpdate.as_view(),name="book_update"),
  path('delete/<int:pk>', views.BookDelete.as_view(),name="book_delete"),
    ]

# urlpatterns = [
#     path('',views.BookList.as_view(),name="book_list"),
#     # path('admin/', admin.site.urls),
#     # # path('Registration/',StudReg,name='studentReg')
#     # path('create/',bookcreate,name='create'),
#     #
#     # path('bookedit/<int:pk>',editbook,name="bookedit"),
#     # path('bookview/<int:pk>',viewbook,name="bookview"),
#     # path('bookdel/<int:pk>',delbook,name="bookdel"),
# ]
