# Generated by Django 3.2.5 on 2021-12-17 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('Std', 'Student'), ('Tcr', 'Teacher'), ('Adm', 'Admin')], default='Std', max_length=3),
        ),
    ]
