from django.contrib import admin
from user.models import Appointment, Payment, ChatRoom, Chat


# Register your models here.

admin.site.register(Payment)
admin.site.register(ChatRoom)
admin.site.register(Chat)
admin.site.register(Appointment)