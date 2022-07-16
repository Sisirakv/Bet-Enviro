from django.contrib import admin

from web.models import Category, Gallery, Contact, Product

# Register your models here.

admin.site.register(Gallery)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Product)