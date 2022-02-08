# Generated by Django 4.0 on 2022-01-12 22:13

from django.db import migrations, models
import main.images_rename


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_remove_employee_first_name_remove_employee_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_pic',
            field=models.ImageField(default='default.png', null=True, upload_to=main.images_rename.path_and_rename('')),
        ),
    ]