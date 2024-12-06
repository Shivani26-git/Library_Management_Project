# Generated by Django 5.0.1 on 2024-01-17 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_edition',
            field=models.CharField(default='1st Edition', max_length=255),
        ),
        migrations.AddField(
            model_name='book',
            name='book_price',
            field=models.CharField(default='00', max_length=25),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher_name',
            field=models.CharField(default='XYZ', max_length=255),
        ),
        migrations.AddField(
            model_name='book',
            name='type_book',
            field=models.CharField(default='Generel', max_length=255),
        ),
    ]