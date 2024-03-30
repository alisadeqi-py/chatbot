from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from django.urls import path

urlpatterns = [
    # jwt
    path('api/jwt/create', TokenObtainPairView.as_view(), name='jwt_obtain_pair'),
    path('api/jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('api/jwt/verify/', TokenVerifyView.as_view(), name='jwt_verify'),
]
