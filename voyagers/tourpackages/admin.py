from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)


class AttractionAdmin(admin.ModelAdmin):
    list_display = ("attractionName", "city",)


admin.site.register(Attraction, AttractionAdmin)
admin.site.register(Location)
admin.site.register(Package)
