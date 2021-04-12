from django.test import TestCase

# Create your tests here.
from datetime import datetime
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import Group
from .models import User, Task

class TasklistTests(APITestCase):
    def setUp(self):
        # create groups
        admin_group = Group.objects.create(name='Admin')

        user_group = Group.objects.create(name='User')

        # create users

        # user admin
        admin_user = User.objects.create(
          email = 'paulmena14@gmail.com',
          username = 'paulspartan014',
          first_name = 'Paul',
          last_name = 'Mena'
        )
        admin_group.groups.add(admin_group)
        admin_user_save()

        # user 1
        admin_user = User.objects.create(
          email = 'karlapuc@gmail.com',
          username = 'karly12',
          first_name = 'Karla',
          last_name = 'Puc'
        )
        admin_group.groups.add(user_group)
        admin_user_save()
        
        # user 2
        admin_user = User.objects.create(
          email = 'josesantos@gmail.com',
          username = 'XibalbaKetzal',
          first_name = 'Jose',
          last_name = 'Santos'
        )
        admin_group.groups.add(user_group)
        admin_user_save()

