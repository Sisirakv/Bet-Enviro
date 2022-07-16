from tabnanny import verbose
from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.utils.text import slugify

# Create your models here.

class Gallery(models.Model):
    image = VersatileImageField('Image',upload_to='images/testimagemodel/')

    class Meta:
        verbose_name_plural =("Gallery")

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(max_length=255)
    is_active  = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = ("Categories")

    def __str__(self):
        return str(self.category_name)

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_image = VersatileImageField('Image',upload_to='images/products/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name