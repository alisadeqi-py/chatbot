from rest_framework import generics
from .models import Customers
from .serializers import CustomersSerializer


class CustomersAPIView(generics.ListCreateAPIView):
    queryset = Customers.objects.all()
    serializer_class = CustomersSerializer
    