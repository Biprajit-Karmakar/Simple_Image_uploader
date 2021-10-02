from django.db import models

# Create your models here.


class IMAGE(models.Model):
    photo = models.ImageField(upload_to="myimages", height_field=None, width_field=None, max_length=None)
    date  = models.DateTimeField(auto_now_add=True)