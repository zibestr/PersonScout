# Generated by Django 5.1.3 on 2024-11-09 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_customuser_preferred_speciality'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='preferred_speciality',
            new_name='speciality',
        ),
    ]
