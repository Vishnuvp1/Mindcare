# Generated by Django 4.0.1 on 2022-01-31 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychologist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='psychologist',
            name='core_skills',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='psychologist',
            name='language',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='psychologist',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10),
        ),
    ]
