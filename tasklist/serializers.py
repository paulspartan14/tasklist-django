from rest_framework import serializers
from django.contrib.auth.models import Group
from .models import User, Task

class UserSerializer(serializers.ModelSerializer):

    # Ver los campos que estan numericos y muestran los valores del array
    groups = serializers.SlugRelatedField(
            many=True,
            read_only=True,
            slug_field='name',
    )
    
    class Meta:
        model = User
        exclude = ['password', 'user_permissions', 'last_login', 'is_staff', 'date_joined', 'is_superuser', 'is_active']

# Serializador para limitar los campos que el usuario puede enviar al hacer un POST
class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

# los campos que serán necesarios para crear un usuario seran username y password
class UserCreateSerializer(serializers.ModelSerializer):
    extra_kwargs = { 'password': { 'write_only': True}}

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']

    # poner seguridad al crear un usuario y que su contraseña se encripte
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user

class GroupSerializer(serializers.ModelSerializer):

    # ver permisos que tiene asignado el grupo
    permissions = serializers.SlugRelatedField(
            many=True,
            read_only=True,
            slug_field='codename',
    )

    class Meta:
        model = Group
        exclude = []
        
class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        exclude = []
