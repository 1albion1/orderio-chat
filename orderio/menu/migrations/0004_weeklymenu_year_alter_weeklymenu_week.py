# Generated by Django 4.0 on 2021-12-31 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_remove_menu_is_holiday'),
    ]

    operations = [
        migrations.AddField(
            model_name='weeklymenu',
            name='year',
            field=models.IntegerField(default=2021),
        ),
        migrations.AlterField(
            model_name='weeklymenu',
            name='week',
            field=models.IntegerField(default=52, unique=True),
        ),
    ]
