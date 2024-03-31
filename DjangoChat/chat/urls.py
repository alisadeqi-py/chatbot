from django.urls import path
from .views import ChatCreateAPIView, ChatDeleteAPIView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
    path('api/chats/', ChatCreateAPIView.as_view(), name='chat-create'),
    path('api/chats/<int:pk>/', ChatDeleteAPIView.as_view(), name='chat-delete'),
]
