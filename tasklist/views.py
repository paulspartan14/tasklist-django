from django.shortcuts import render
from rest_framework import viewsets, generics
from django.contrib.auth.models import Group

from .serializers import GroupSerializer, UserSerializer
from .models import User, Task

# Create your views here.

class GroupView(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filterset_fields = []
    search_fields = ['username', 'email']
    ordering_fields = ['id', 'email', 'username']
    ordering = ['-date_joined']
