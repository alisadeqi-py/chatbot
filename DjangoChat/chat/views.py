from django.shortcuts import render
from django.utils.safestring import mark_safe
from rest_framework import generics, status
from .models import Chat
from .serializers import ChatSerializer
from rest_framework.response import Response
import json

def index(request):
    return render(request, "chat/index.html")


def room(request, room_name):

    user_name = request.user.username
    #print(user_name)

    return render(request, "chat/room.html",
                  {"room_name": room_name,
                   "user_name": mark_safe(json.dumps(user_name))})


class ChatCreateAPIView(generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class ChatDeleteAPIView(generics.DestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)