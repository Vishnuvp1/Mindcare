# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'user/room.html')

def room(request, room_name):
    return render(request, 'user/chat.html', {
        'room_name_json' : mark_safe(json.dumps(room_name)),
        'username' : mark_safe(json.dumps(request.user.first_name)), 
    })