# Generated by Django 5.0.1 on 2024-02-02 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0031_b_issue_book_name_b_issue_firstname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='b_issue',
            name='mobile',
            field=models.IntegerField(default='0000000000'),
        ),
    ]
