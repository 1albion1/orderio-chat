# Generated by Django 4.0 on 2021-12-29 15:38

from django.db import migrations, models
import main.images_rename


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0002_meal_meal_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='meal',
            name='meal_img',
            field=models.ImageField(blank=True, default='meal-default.png', null=True, upload_to=main.images_rename.path_and_rename('')),
        ),
        migrations.AlterField(
            model_name='meal',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
