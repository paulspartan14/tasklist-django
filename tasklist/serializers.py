from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        exclude = ['password', 'user_permissions']

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        exclude = []

