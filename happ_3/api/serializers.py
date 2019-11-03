from rest_framework import serializers
from .models import caracteristiques,lieux,usagers,vehicules, acc_data


# Serializers to convert the data to a json format

class caracteristiquesSerializer(serializers.ModelSerializer):
    

    class Meta:
        model = caracteristiques
        fields = '__all__'

class lieuxSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  lieux
        fields = '__all__'
        
class usagersSerializer(serializers.ModelSerializer):
    class Meta:
        model = usagers
        fields = '__all__'
        
class vehiculesSerializer(serializers.ModelSerializer):
    class Meta:
        model  = vehicules
        fields = '__all__'
    
class accidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = acc_data
        fields = '__all__'