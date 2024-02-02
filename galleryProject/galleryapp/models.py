from django.db import models

# Create your models here.


class Image(models.Model):
    # title=models.CharField(max_length=255)
    photo = models.ImageField(upload_to="user_image")
    date = models.DateField(auto_now_add=True)
