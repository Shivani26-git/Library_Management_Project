# Generated by Django 5.0.1 on 2024-01-19 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_alter_users_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='mobile',
            field=models.CharField(max_length=255),
        ),
    ]
