# Generated by Django 3.1.7 on 2021-03-18 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(blank=True, choices=[('1', '1 месяц'), ('2', '2 месяц'), ('3', '3 месяц'), ('4', '4 месяц'), ('5', '5 месяц'), ('6', '6 месяц'), ('7', '7 месяц')], max_length=50, null=True, verbose_name='Месяц')),
                ('category', models.CharField(blank=True, choices=[('1', 'Помогите с темой курса'), ('2', 'Помогите с домашним заданием'), ('3', 'Сходим пообедать'), ('4', 'Кто хочет в магазин')], max_length=100, null=True, verbose_name='Категория')),
                ('group_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='Номер группы')),
                ('course_program', models.CharField(blank=True, choices=[('Back', 'Backend-разработчик'), ('Front', 'Frontend-разработчик'), ('IOS', 'iOS-разработчик'), ('Android', 'Android-разработка'), ('Ui/Ux', 'UX/UI Designer'), ('English', 'IT Английский')], max_length=100, null=True, verbose_name='Программа курса')),
                ('teacher', models.CharField(blank=True, choices=[('Back', 'Backend-разработчик'), ('Front', 'Frontend-разработчик'), ('IOS', 'iOS-разработчик'), ('Android', 'Android-разработка'), ('Ui/Ux', 'UX/UI Designer'), ('English', 'IT Английский')], max_length=100, null=True, verbose_name='Учитель')),
                ('problem_title', models.TextField(verbose_name='Дайте название проблеме')),
                ('problem_description', models.TextField(verbose_name='Опишите проблему')),
                ('file', models.FileField(upload_to='media', verbose_name='Прикрепите файл')),
            ],
        ),
    ]
