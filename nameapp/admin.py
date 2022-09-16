from django.contrib import admin

# Register your models here.
from .models import mouse_species,mouse_type

admin.site.register(mouse_type)
admin.site.register(mouse_species)