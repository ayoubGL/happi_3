"""happ_3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'api'

router = DefaultRouter()

router.register(r'caracteristiques', CaracteristiquesViewset)
router.register(r'lieux', lieuxViewset)
router.register(r'usagers', usagersViewset)
router.register(r'vehicules', vehiculesViewset)
router.register(r'accident', AccidentViewset)

urlpatterns = router.urls
urlpatterns += staticfiles_urlpatterns()



