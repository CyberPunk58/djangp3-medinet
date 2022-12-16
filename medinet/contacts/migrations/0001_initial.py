# Generated by Django 4.1 on 2022-11-05 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('category', models.CharField(choices=[('Администрация', 'Администрация'), ('Менеджеры', 'Менеджеры'), ('Администраторы сайта', 'Администраторы сайта'), ('Пользователи', 'Пользователи')], default='Пользователи', max_length=25)),
                ('job_title', models.CharField(max_length=50, verbose_name='Должность')),
                ('ext_number', models.CharField(max_length=5, verbose_name='Внутренний телефон')),
                ('phine_number', models.CharField(max_length=12, verbose_name='Городской телефон')),
            ],
            options={
                'verbose_name': 'Номера телефонов',
                'verbose_name_plural': 'Номера телефонов',
            },
        ),
    ]
