from django.contrib.auth.models import AbstractUser
from django.db import models
from customer.models import Customers
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    address = models.CharField(max_length=255, blank=True, null=True)
    open = models.DateTimeField(null=True, blank=True)
    close = models.DateTimeField(null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True)
    chat_bot_name = models.CharField(max_length=5, default = 'مریم')
