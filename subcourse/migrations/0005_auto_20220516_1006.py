# Generated by Django 3.2 on 2022-05-16 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subcourse', '0004_auto_20220509_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='subcourse',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]