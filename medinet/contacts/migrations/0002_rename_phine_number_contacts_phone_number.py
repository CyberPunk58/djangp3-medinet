# Generated by Django 4.1 on 2022-11-05 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contacts',
            old_name='phine_number',
            new_name='phone_number',
        ),
    ]