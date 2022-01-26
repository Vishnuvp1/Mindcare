from distutils.command.upload import upload
from django.db import models

# Create your models here.

GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female'),
)

class Psychologist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=50, unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField(
        auto_now_add=False, auto_now=False, blank=True)
    address = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    resume = models.ImageField(upload_to='Resume')
    certificate = models.ImageField(upload_to='Certificate')
    password = models.CharField(max_length=20, blank=False)

    # Required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
