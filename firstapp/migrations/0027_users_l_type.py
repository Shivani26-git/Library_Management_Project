# Generated by Django 5.0.1 on 2024-01-31 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0026_remove_login_date_remove_login_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='l_type',
            field=models.CharField(default='xyz', max_length=255),
        ),
    ]
