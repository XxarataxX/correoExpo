from rest_framework import serializers
from .models import EmailRequest, EmailRequest2

class EmailRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailRequest
        fields = ['recipient', 'nombre', 'telefono', 'asunto', 'mensaje']
        extra_kwargs = {
            'nombre': {'required': False},
            'telefono': {'required': False},
            'asunto': {'required': False},
            'mensaje': {'required': False}
        }

class EmailRequest2Serializer(serializers.ModelSerializer):
    class Meta:
        model = EmailRequest2
        fields = ['recipient', 'nombre', 'telefono', 'empresa', 'stand', 'mensaje']
        extra_kwargs = {
            'nombre': {'required': False},
            'telefono': {'required': False},
            'empresa': {'required': False},
            'stand': {'required': False},
            'mensaje': {'required': False}
        }