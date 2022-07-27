from django.contrib import admin

from web.models import Category, Gallery, Contact, Product, Blog, Client, Service, subService, ServiceLocator, District, LocalArea
from .models import *

# Register your models here.

admin.site.register(Gallery)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Blog)
admin.site.register(Client)
# admin.site.register(Service)
# admin.site.register(subService)
admin.site.register(ServiceLocator)
admin.site.register(District)
admin.site.register(LocalArea)
admin.site.register(Enquiry)
