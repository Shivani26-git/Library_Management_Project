# Generated by Django 5.0.1 on 2024-01-17 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('book_name', models.CharField(max_length=255)),
                ('writer_name', models.CharField(max_length=255)),
            ],
        ),
    ]

