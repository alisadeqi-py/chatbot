# In urls.py
from django.urls import path
from .views import CarCreateAPIView, CarFeaturesAPIView, CarUpdateAPIView, UserCarsListAPIView


urlpatterns = [
    path('api/create/', CarCreateAPIView.as_view(), name='car-create'),
    path('api/carfeatures/', CarFeaturesAPIView.as_view(), name = 'carfeatures-list-create'),
    path('api/update/<int:pk>/', CarUpdateAPIView.as_view(), name='car-update'),
path('api/users/<int:user_id>/cars/', UserCarsListAPIView.as_view(), name='user-cars-list'),
]
