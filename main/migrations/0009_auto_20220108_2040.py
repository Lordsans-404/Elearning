# Generated by Django 3.2.5 on 2022-01-08 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_course_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='teacher_id',
        ),
        migrations.AddField(
            model_name='course',
            name='teacher_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.teacher'),
        ),
    ]
