# Generated by Django 3.2.5 on 2022-01-15 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_attendancereq_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancereq',
            name='start_time',
            field=models.DateTimeField(default=models.DateTimeField(auto_now_add=True)),
        ),
    ]
