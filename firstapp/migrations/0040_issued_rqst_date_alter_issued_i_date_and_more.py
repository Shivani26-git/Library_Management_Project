# Generated by Django 5.0.1 on 2024-02-07 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0039_alter_issued_i_date_alter_issued_r_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='issued',
            name='rqst_date',
            field=models.DateField(default='1999-01-01'),
        ),
        migrations.AlterField(
            model_name='issued',
            name='i_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='issued',
            name='r_date',
            field=models.DateField(default='1999-01-01'),
        ),
    ]
