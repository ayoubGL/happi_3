from django.contrib import admin
from .models import caracteristiques,lieux,usagers,vehicules, acc_data

# Register the  models in to the admin page
admin.site.register(caracteristiques)
admin.site.register(lieux)
admin.site.register(usagers)
admin.site.register(vehicules)
admin.site.register(acc_data)