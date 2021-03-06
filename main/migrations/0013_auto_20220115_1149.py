# Generated by Django 3.2.5 on 2022-01-15 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_attendance_student_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceReq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.DateTimeField()),
                ('closed_time', models.DateTimeField()),
                ('is_closed', models.BooleanField(default=False)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
            ],
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
    ]
