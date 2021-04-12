from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        exclude = ['password', 'user_permissions', 'last_login', 'is_staff', 'date_joined', 'is_superuser', 'is_active']

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        exclude = []

