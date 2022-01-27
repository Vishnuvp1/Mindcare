from django.db import models
from accounts.models import Account

# Create your models here.

GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female'),
)


class Psychologist(models.Model):
    psychologist = models.OneToOneField(Account, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(
        auto_now_add=False, auto_now=False, blank=True)
    address = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    resume = models.ImageField(upload_to='Resume')
    certificate = models.ImageField(upload_to='Certificate')

    def __str__(self):
        return self.address
