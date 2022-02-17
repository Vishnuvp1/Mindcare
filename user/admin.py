from django.contrib import admin
from user.models import Appointment, Payment


# Register your models here.

admin.site.register(Payment)
admin.site.register(Appointment)