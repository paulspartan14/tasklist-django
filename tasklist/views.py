from django.shortcuts import render
from rest_framework import viewsets, generics
from django.contrib.auth.models import Group

from .serializers import GroupSerializer, UserSerializer, UserInfoSerializer, UserCreateSerializer, TaskSerializer
from .models import User, Task
from .permissions import UserPermission

# Create your views here.

# Views for groups
class GroupViewSet(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# Views For User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Permisos
    permission_classes = (UserPermission, )

    filterset_fields = []
    search_fields = ['username', 'email']
    ordering_fields = ['id', 'email', 'username']
    ordering = ['-date_joined']

    # Poder editar solo las propiedades personales de cada usuario
    def get_queryset(self):
        id = self.request.user.id
        return User.objects.filter(id=id)

    # si el metodo es alguno de estos entonces devuelve un serializador en especifico
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserInfoSerializer
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

# Views For Tasks
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # Solamente retornará las tareas del usuario actual
    def get_queryset(self):
        id = self.request.user.id
        return Task.objects.filter(owner=id)