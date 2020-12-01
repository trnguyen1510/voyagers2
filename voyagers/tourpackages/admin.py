from django.contrib import admin

# Register your models here.

from .models import *




class AttractionAdmin(admin.ModelAdmin):
    list_display = ("attractionName", "city",)


admin.site.register(Attraction, AttractionAdmin)

