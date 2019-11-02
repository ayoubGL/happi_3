from django.contrib import admin
from .models import caracteristiques,lieux,usagers,vehicules

# Register your models here.
admin.site.register(caracteristiques)
admin.site.register(lieux)
admin.site.register(usagers)
admin.site.register(vehicules)