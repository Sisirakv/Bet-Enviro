from django.db import models
from versatileimagefield.fields import VersatileImageField

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

    class Meta:
        verbose_name_plural =("Contact")

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


class subService(models.Model):
    main_service = models.ForeignKey(Service, on_delete=models.CASCADE)
    sub_name = models.CharField(max_length=200)
    sub_image = VersatileImageField('Image',upload_to='images/sub service/')
    sub_description = models.TextField()

    class Meta:
        verbose_name_plural =("Sub service")
 