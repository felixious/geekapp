# Generated by Django 3.1.7 on 2021-03-16 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, max_length=20, null=True, verbose_name='Birthday'),
        ),
    ]