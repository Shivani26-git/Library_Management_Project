# Generated by Django 5.0.1 on 2024-02-05 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0034_delete_login_book_b_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='b_id',
        ),
    ]
