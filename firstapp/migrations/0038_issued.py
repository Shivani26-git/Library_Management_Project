# Generated by Django 5.0.1 on 2024-02-06 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0037_login_history_delete_issue_requ'),
    ]

    operations = [
        migrations.CreateModel(
            name='issued',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('l_Id', models.CharField(max_length=255)),
                ('m_name', models.CharField(default='0000000000', max_length=255)),
                ('b_Id', models.CharField(default='00', max_length=255)),
                ('book_name', models.CharField(max_length=255, null=True)),
                ('mobile', models.IntegerField(default='0000000000')),
                ('writer_name', models.CharField(max_length=255, null=True)),
                ('publisher_name', models.CharField(max_length=255, null=True)),
                ('i_date', models.DateField()),
                ('r_date', models.DateField(default='1999-01-01')),
            ],
        ),
    ]
