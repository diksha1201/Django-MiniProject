# serializers.py

from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

class ProjectSerializer(serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_client_name(self, obj):
        return obj.client.client_name

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']




