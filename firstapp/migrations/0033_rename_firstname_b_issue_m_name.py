# Generated by Django 5.0.1 on 2024-02-02 01:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0032_b_issue_mobile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='b_issue',
            old_name='firstname',
            new_name='m_name',
        ),
    ]
