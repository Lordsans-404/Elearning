# Generated by Django 3.2.5 on 2022-01-04 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20220103_2008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.classroom')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('absent', 'Absent'), ('present', 'Present')], default='present', max_length=10)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
            ],
        ),
    ]
