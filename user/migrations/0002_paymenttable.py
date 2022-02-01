# Generated by Django 4.0.1 on 2022-02-01 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('title', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, max_length=900)),
            ],
        ),
    ]