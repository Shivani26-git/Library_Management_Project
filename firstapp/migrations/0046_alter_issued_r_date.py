# Generated by Django 5.0.1 on 2024-02-08 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0045_alter_rturn_r_date_alter_rturn_risu_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issued',
            name='r_date',
            field=models.DateField(null=True),
        ),
    ]
