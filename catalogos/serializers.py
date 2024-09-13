from .models import *
from rest_framework import serializers

#serializer para pais


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['nombre', 'codigo']

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = ['nombre', 'pais', 'codigo','active']

class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['nombre', 'departamento', 'codigo', 'active']                
