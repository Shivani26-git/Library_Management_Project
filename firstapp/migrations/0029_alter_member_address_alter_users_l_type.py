# Generated by Django 5.0.1 on 2024-02-01 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0028_alter_users_l_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='address',
            field=models.TextField(default='0000000000', max_length=255),
        ),
        migrations.AlterField(
            model_name='users',
            name='l_type',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
