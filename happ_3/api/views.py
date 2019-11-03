from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import generics
from .models import caracteristiques,lieux,usagers,vehicules, acc_data
from .serializers import caracteristiquesSerializer, lieuxSerializer,usagersSerializer, vehiculesSerializer,accidentSerializer
from rest_framework import viewsets

# custom pagination used to paginate through the different tables

class custumpagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = page_size
    max_page_size = 100
    
    def get_paginated_response(self, data):
        return Response(
            {
                'link':{
                    'next':self.get_next_link(),
                    'previous':self.get_previous_link(),
                },
                'total_object' : self.page.paginator.count,
                'page_size':self.page_size,
                'records':data
            }
        )
    
# custom pagination used to paginate the accident data
class paginationAccident(PageNumberPagination):
    page_size = 3
    page_query_param = page_size
    max_page_size = 5
    
    def get_paginated_response(self, data):
        return Response({
            'link':{
                'next':self.get_next_link(),
                'previous':self.get_previous_link()
            },
            'total_object':self.page.paginator.count,
            'page_size':self.page_size,
            'Accident':data
        })

    
# View set to link the fetched data with serializers

class CaracteristiquesViewset(viewsets.ModelViewSet):
    queryset = caracteristiques.objects.all()
    serializer_class = caracteristiquesSerializer
    pagination_class  = custumpagination

class lieuxViewset(viewsets.ModelViewSet):
    queryset = lieux.objects.all()
    serializer_class = lieuxSerializer
    pagination_class  = custumpagination

class usagersViewset(viewsets.ModelViewSet):
    queryset = usagers.objects.all()
    serializer_class = usagersSerializer
    pagination_class  = custumpagination

class vehiculesViewset(viewsets.ModelViewSet):
    queryset = vehicules.objects.all()
    serializer_class = vehiculesSerializer
    pagination_class  = custumpagination

class AccidentViewset(viewsets.ModelViewSet):
    queryset = acc_data.objects.all()
    serializer_class = accidentSerializer
    pagination_class = paginationAccident

