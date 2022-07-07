from django.urls import path
from . import views


app_name='web'

urlpatterns = [
    path("",views.base),
    path("product",views.product,name='product'),
    path("contact",views.contact,name='contact'),
    path("gallery",views.gallery,name='gallery'),
    path("blog",views.blog,name='blog'), 
    path("services",views.services,name='services'), 


]