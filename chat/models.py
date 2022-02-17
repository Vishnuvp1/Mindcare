import datetime
from django.db import models

from accounts.models import Account

# Create your models here.


class Message(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name

    def last_10_messages(self):
        return Message.objects.order_by('-timestamp').all()[:10]
