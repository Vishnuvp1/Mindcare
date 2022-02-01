# Generated by Django 4.0.1 on 2022-01-31 05:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Psychologist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='Profile_image')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=10)),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth (MM/DD/YYYY)')),
                ('department', models.CharField(max_length=255)),
                ('experience', models.CharField(max_length=255)),
                ('resume', models.ImageField(upload_to='Resume')),
                ('certificate', models.ImageField(upload_to='Certificate')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
