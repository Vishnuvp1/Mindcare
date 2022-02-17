import re
from django.db import models
from django.forms import CharField
from accounts.models import Account
from datetime import datetime

# Create your models here.


class Payment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100)
    amound_paid = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_method



class Appointment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    date = models.CharField(max_length=500)
    time = models.CharField(max_length=500)