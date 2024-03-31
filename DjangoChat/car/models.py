from django.db import models


class CarFeatures(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):

    user = models.ForeignKey("account.CustomeUser", on_delete=models.CASCADE)
    model = models.CharField(max_length=30)
    color = models.CharField(max_length=10, null=True, blank=True)
    make = models.CharField(max_length=10)
    features = models.ManyToManyField(CarFeatures, related_name='cars', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    price = models.BigIntegerField()

    def __str__(self):
        return self.model
