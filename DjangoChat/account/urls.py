from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import signUp
from django.urls import path

urlpatterns = [
    # registration
    path('api/signup/', signUp.as_view(), name='signup'),
    # jwt
    path('api/jwt/create', TokenObtainPairView.as_view(), name='jwt_obtain_pair'),
    path('api/jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('api/jwt/verify/', TokenVerifyView.as_view(), name='jwt_verify'),
]
