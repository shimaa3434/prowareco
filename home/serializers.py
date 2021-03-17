from rest_framework import serializers
from .models import Client, Phone, Info, Service

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["name", "email", "phone", 'message']


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        fields = ['number']

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['place', 'phone', 'email']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['name', 'icon', 'dec']