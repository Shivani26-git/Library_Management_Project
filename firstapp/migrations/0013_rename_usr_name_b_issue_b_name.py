# Generated by Django 5.0.1 on 2024-01-24 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0012_rename_userid_b_issue_l_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='b_issue',
            old_name='usr_name',
            new_name='b_name',
        ),
    ]
