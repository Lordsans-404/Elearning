# Generated by Django 3.2 on 2022-02-05 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20220205_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancereq',
            name='closed_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='attendancereq',
            name='start_time',
            field=models.DateTimeField(),
        ),
    ]
