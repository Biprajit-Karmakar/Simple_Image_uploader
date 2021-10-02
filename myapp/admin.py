from django.contrib import admin
from .models import IMAGE
# Register your models here.

@admin.register(IMAGE)
class IMAGEadmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'date']