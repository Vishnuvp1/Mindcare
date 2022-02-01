import re
from django.db import models
from accounts.models import Account

# Create your models here.



class Payment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=100)
    amound_paid = models.CharField(max_length=100) 
    status = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_method