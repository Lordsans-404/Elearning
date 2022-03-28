# Generated by Django 3.2 on 2022-03-27 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20220205_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content1', models.CharField(max_length=255)),
                ('content2', models.CharField(blank=True, max_length=255, null=True)),
                ('file', models.FileField(upload_to='uploads_file/')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
            ],
        ),
    ]
