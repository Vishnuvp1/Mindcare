# Generated by Django 4.0.1 on 2022-01-26 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_phone_number_account_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(blank=True, max_length=50, unique=True),
        ),
    ]