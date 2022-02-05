from django.db import models
from django.urls import reverse
from accounts.models import Account

# Create your models here.

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
)


class Psychologist(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        upload_to='Profile_image', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    date_of_birth = models.DateField("Date of Birth (MM/DD/YYYY)",
                                     auto_now_add=False, auto_now=False)
    department = models.CharField(max_length=255)
    fees = models.IntegerField(default=700)
    languages = models.CharField(max_length=255, blank=True, null=True)
    skills = models.CharField(max_length=255, blank=True, null=True)
    experience = models.CharField(max_length=255)
    resume = models.ImageField(upload_to='Resume')
    certificate = models.ImageField(upload_to='Certificate')

    def get_url(self):
        return reverse('psychologist-details', args=[self.id])

    def __str__(self):
        return self.account.email


class ConsultTime(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    date = models.CharField(max_length=300, blank=True, null=True)
    time = models.CharField(max_length=300, blank=True, null=True)

    def __str__(self):
        return self.date
