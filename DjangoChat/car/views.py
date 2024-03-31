from rest_framework import generics, status
from rest_framework.response import Response
from .models import Car, CarFeatures
from .serializers import CarSerializer, CarFeaturesSerializer


class CarCreateAPIView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarFeaturesAPIView(generics.ListCreateAPIView):
    queryset = CarFeatures.objects.all()
    serializer_class = CarFeaturesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CarUpdateAPIView(generics.UpdateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def put(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)


class UserCarsListAPIView(generics.ListAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        user_id = self.kwargs['user_id']  # Assuming 'user_id' is passed in URL pattern
        return Car.objects.filter(user_id=user_id)
