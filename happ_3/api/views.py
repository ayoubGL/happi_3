from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import generics
from .models import caracteristiques,lieux,usagers,vehicules, acc_data
from .serializers import caracteristiquesSerializer, lieuxSerializer,usagersSerializer, vehiculesSerializer,accidentSerializer
from rest_framework import viewsets



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

    
# if we want to user viewset that make things easy
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




# if we want to empliment each view
# class ListCaracteristiques(generics.ListCreateAPIView):
#     queryset = caracteristiques.objects.all()
#     serializer_class = caracteristiquesSerializer
#     #lookup_field = 'Num_Acc'
#     pagination_class  = custumpagination

# class DetailCaracteristiques(generics.RetrieveUpdateDestroyAPIView):
#     queryset = caracteristiques.objects.all()
#     serializer_class = caracteristiquesSerializer
#     pagination_class  = custumpagination
    
    
    
# class ListLieux(generics.ListCreateAPIView):
#     queryset = lieux.objects.all()
#     serializer_class = lieuxSerializer
#     pagination_class  = custumpagination
# class DetailLieux(generics.RetrieveUpdateDestroyAPIView):
#     queryset = lieux.objects.all()
#     serializer_class = lieuxSerializer

    
# class ListUsagers(generics.ListCreateAPIView):
#     queryset = usagers.objects.all()
#     serializer_class = usagersSerializer
#     pagination_class  = custumpagination
# class DetailUsagers(generics.RetrieveUpdateDestroyAPIView):
#     queryset = usagers.objects.all()
#     serializer_class = usagersSerializer


    
# class ListVehicules(generics.ListCreateAPIView):
#     queryset = vehicules.objects.all()
#     seriliazer_class = vehiculesSerializer
#     pagination_class  = custumpagination
# class DetailVehicules(generics.RetrieveUpdateDestroyAPIView):
#     queryset = vehicules.objects.all()
#     serializer_class = vehiculesSerializer
    