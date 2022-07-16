from django.contrib import admin

from web.models import Category, Gallery, Contact, Product
from .models import *

# Register your models here.

admin.site.register(Gallery)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Blog)
admin.site.register(Client)
admin.site.register(Service)
admin.site.register(subService)
admin.site.register(Service_locator)
