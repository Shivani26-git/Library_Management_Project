# Generated by Django 5.0.1 on 2024-01-24 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0016_book_b_qty'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='lastname',
        ),
    ]
