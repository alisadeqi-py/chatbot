from rest_framework import serializers
from .models import Car, CarFeatures


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarFeaturesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarFeatures
        fields = '__all__'
