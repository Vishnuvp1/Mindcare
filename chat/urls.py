# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='chat-room'),
    path('<str:room_name>/', views.room, name='room'),
]