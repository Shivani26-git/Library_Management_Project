# Generated by Django 5.0.1 on 2024-01-18 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_book_book_edition_book_book_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('c_password', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='book_edition',
            field=models.CharField(default='1st', max_length=255),
        ),
    ]