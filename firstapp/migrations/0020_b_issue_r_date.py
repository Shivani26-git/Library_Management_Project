# Generated by Django 5.0.1 on 2024-01-25 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0019_alter_member_d_o_b'),
    ]

    operations = [
        migrations.AddField(
            model_name='b_issue',
            name='r_date',
            field=models.DateField(default='1999-01-01'),
        ),
    ]
