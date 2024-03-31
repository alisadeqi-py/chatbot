# In urls.py
from django.urls import path
from .views import CustomersAPIView

urlpatterns = [
    path('api/create/', CustomersAPIView.as_view(), name='customers-list-create'),
]
