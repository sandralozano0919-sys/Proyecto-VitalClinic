from rest_framework import serializers
from .models import PQRS

class PQRSSerializer(serializers.ModelSerializer):
    class Meta:
        model = PQRS
        fields = "__all__"  # Puedes especificar campos si quieres
