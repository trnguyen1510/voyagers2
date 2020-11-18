from django.contrib import admin

# Register your models here.
from .models import User_Profile

@admin.register(User_Profile)
class User_ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'Address', 'Country')

