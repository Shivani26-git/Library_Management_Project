# Generated by Django 5.0.1 on 2024-02-08 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0042_rturn'),
    ]

    operations = [
        migrations.AddField(
            model_name='rturn',
            name='I_Id',
            field=models.IntegerField(default='0001'),
        ),
    ]
