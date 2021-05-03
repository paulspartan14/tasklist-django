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
        admin_user.groups.add(admin_group)
        admin_user.save()

        # user 1
        admin_user = User.objects.create(
          email = 'karlapuc@gmail.com',
          username = 'karly12',
          first_name = 'Karla',
          last_name = 'Puc'
        )
        admin_user.groups.add(user_group)
        admin_user.save()
        
        # user 2
        admin_user = User.objects.create(
          email = 'josesantos@gmail.com',
          username = 'XibalbaKetzal',
          first_name = 'Jose',
          last_name = 'Santos'
        )
        admin_user.groups.add(user_group)
        admin_user.save()

    def TestAuth(self):
        response = self.client.get('/api/auth/groups/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        data = { 'username': 'paul', 'password': '12345' }
        response = self.client.post('/api/auth/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        token = response.json()['access']

        self.client.credentials(HTTP_AUTHORIZATION= 'Bearer %s'% token)
        response = self.client.get('/api/auth/groups/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.client.login(username = 'paul', password = 'paulspartan44')
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


