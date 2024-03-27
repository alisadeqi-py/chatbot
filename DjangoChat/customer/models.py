from django.db import models
from car.models import Car
from django.contrib.auth.models import User
# Create your models here.


class Customers(models.Model):
    dealer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=15, unique=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'M'), ('Female', 'F')], default='M')
    car_intrested = models.ManyToManyField(Car)


    def __str__(self):

        return str(f'{self.name}-{self.id}')

