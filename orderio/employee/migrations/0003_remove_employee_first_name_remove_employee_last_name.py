# Generated by Django 4.0 on 2022-01-02 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='last_name',
        ),
    ]
