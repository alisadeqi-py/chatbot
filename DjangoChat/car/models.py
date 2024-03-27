from django.db import models
from django.contrib.auth.models import User


class CarFeatures(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=10)
    make = models.CharField(max_length=10)
    features = models.ManyToManyField(CarFeatures, related_name='cars')
    description = models.TextField()
    price = models.BigIntegerField()

    def __str__(self):
        return self.model
