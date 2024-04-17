# from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer
from rest_framework import generics
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

from rest_framework import generics
from .models import Client, Project
from .serializers import ClientSerializer, ProjectSerializer

class UserDeleteAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProjectDeleteAPIView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ClientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        client_id = self.request.data.get('client_id')
        serializer.save(
            created_by=self.request.user,
            client_id=client_id,
            users=User.objects.filter(id__in=self.request.data.get('users'))
        )

class ProjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# class UserDeleteAPIView(generics.DestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class ProjectDeleteAPIView(generics.DestroyAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

# class ClientListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer

# class ClientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer

# class ProjectListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer

#     def perform_create(self, serializer):
#         client_id = self.request.data.get('client_id')
#         serializer.save(
#             created_by=self.request.user,
#             client_id=client_id,
#             users=User.objects.filter(id__in=self.request.data.get('users'))
#         )

# class ProjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer