# Generated by Django 5.0.1 on 2024-02-02 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0030_alter_member_d_o_b'),
    ]

    operations = [
        migrations.AddField(
            model_name='b_issue',
            name='book_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='b_issue',
            name='firstname',
            field=models.CharField(default='0000000000', max_length=255),
        ),
        migrations.AddField(
            model_name='b_issue',
            name='publisher_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='b_issue',
            name='writer_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]