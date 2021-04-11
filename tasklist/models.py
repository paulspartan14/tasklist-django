from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)

class Task(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
