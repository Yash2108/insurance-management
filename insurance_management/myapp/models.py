from django.db import models

# Create your models here.
class Insurances(models.Model):
    photo=models.ImageField(upload_to="saved_images")
    date= models.DateTimeField(auto_now_add=True)