# Generated by Django 3.2.5 on 2022-01-15 04:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20220115_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('absent', 'Absent'), ('present', 'Present')], default='present', max_length=10)),
                ('attendanceReq_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.attendancereq')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
        ),
    ]
