# Generated by Django 3.2.5 on 2022-01-08 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_attendance_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
