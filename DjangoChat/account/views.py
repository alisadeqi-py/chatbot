from django.shortcuts import render
from rest_framework import generics
from .serializers import signUpSerializer
from rest_framework import status
from rest_framework.response import Response
# Create your views here.



class signUp(generics.CreateAPIView):
    serializer_class = signUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = signUpSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            data = {
                'email': serializer.validated_data['email']

            }
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
