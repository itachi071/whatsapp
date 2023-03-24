from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(Upload_Data)
class Data(admin.ModelAdmin):
    list_display = ['Name','File'] 
