from .models import *
from rest_framework import serializers

#serializer para pais


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['nombre', 'codigo']
