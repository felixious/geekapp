# Generated by Django 3.1.7 on 2021-03-17 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, max_length=20, null=True, verbose_name='Birthday'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Phone number'),
        ),
    ]
