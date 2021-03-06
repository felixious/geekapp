# Generated by Django 3.1.7 on 2021-03-15 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20210315_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='ratting',
            field=models.DecimalField(decimal_places=1, default=4.1, max_digits=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='rate',
            field=models.IntegerField(),
        ),
    ]
