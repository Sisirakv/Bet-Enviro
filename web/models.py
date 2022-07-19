from tabnanny import verbose
from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.utils.text import slugify

# Create your models here.

class Gallery(models.Model):
    name = models.CharField(max_length=200)
    image = VersatileImageField('Image',upload_to='images/testimagemodel/')

    class Meta:
        verbose_name_plural =("Gallery")

    def __str__(self):
        return self.name

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

    class Meta:
        verbose_name_plural =("Product")

class Blog(models.Model):
    image = VersatileImageField('Image',upload_to='images/blog/')
    heading = models.TextField()
    category = models.TextField(max_length=200)
    date = models.DateField(auto_now_add=True,editable=False)
    content = models.TextField()

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name_plural =("Blog")


class Client(models.Model):
    name = models.CharField(max_length=200)
    image = VersatileImageField('Image',upload_to='images/Client/')

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=200)
    image = VersatileImageField('Image',upload_to='images/service/')
    description = models.TextField()

    class Meta:
        verbose_name_plural =("service")

    def __str__(self):
        return self.name


class subService(models.Model):
    main_service = models.ForeignKey(Service, on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=200)
    sub_image = VersatileImageField('Image',upload_to='images/sub service/')
    sub_description = models.TextField()

    class Meta:
        verbose_name_plural =("Sub service")

class District(models.Model):
    district_name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = ("District")

    def __str__(self):
        return self.district_name

class LocalArea(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE,null= True)
    local_area_name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = ("Local Area")

    def __str__(self):
        return self.local_area_name

class ServiceLocator(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    local_area = models.ForeignKey(LocalArea, on_delete=models.CASCADE)
    center = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.center
 
