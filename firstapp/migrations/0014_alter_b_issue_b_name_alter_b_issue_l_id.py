# Generated by Django 5.0.1 on 2024-01-24 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0013_rename_usr_name_b_issue_b_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='b_issue',
            name='b_name',
            field=models.CharField(default='00', max_length=255),
        ),
        migrations.AlterField(
            model_name='b_issue',
            name='l_Id',
            field=models.CharField(max_length=255),
        ),
    ]
