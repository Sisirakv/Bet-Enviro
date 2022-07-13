from django.db import models
from versatileimagefield.fields import VersatileImageField

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