# Generated by Django 4.0 on 2021-12-29 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='created_for',
            field=models.IntegerField(blank=True, choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wendnesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], default=1, null=True),
        ),
    ]
