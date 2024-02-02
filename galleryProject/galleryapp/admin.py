from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = [ 'photo', 'date','id',]
