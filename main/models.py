from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.base import Model
from django.utils.text import slugify
from django.utils import timezone

# User
class CustomUser(AbstractUser):
    TYPE_CHOICES = (
        ('Std', 'Student'),
        ('Tcr', 'Teacher'),
        ('Adm', 'Admin'),
    )
    user_type = models.CharField(choices=TYPE_CHOICES,default='Std',max_length=3)

# <<<=====================================================================>>>
class Teacher(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    description = models.CharField(max_length=255,null=True, blank=True)

    def __str__(self):
        return self.user.username

class Classroom(models.Model):
    name = models.CharField(max_length=155)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    class_id = models.ForeignKey(Classroom,on_delete=models.SET_NULL,null=True,blank=True)
    
    def __str__(self):
        return self.user.username

class Course(models.Model):
    name = models.CharField(max_length=255,null=True)
    teacher_id = models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True,blank=True)
    class_id = models.ForeignKey(Classroom,on_delete=models.SET_NULL,null=True,blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} Kelas {self.class_id.name}'

    def get_absolute_url(self):
        return '/'

# class SubCourseFile(models.Model):
#     subcourse_id = models.ForeignKey(SubCourse,on_delete=models.CASCADE,null=True)
#     file = models.FileField(upload_to="uploads_file/")


class AttendanceReq(models.Model):
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField()
    closed_time = models.DateTimeField()
    is_closed = models.BooleanField(default=False)

    @property
    def check_time(self):
        start = self.start_time
        closed = self.closed_time
        is_closed = self.is_closed
        noww = timezone.now()
        if is_closed:
            if noww.date() == start.date():
                if noww.time() >= start.time():
                    self.is_closed = True



    def __str__(self):
        return f'{self.course_id} Tanggal {self.date_time.date()} Closed = {self.is_closed}'

    def get_absolute_url(self):
        return f'/my/course-{self.course_id}'

    

class Attendance(models.Model):
    ATTENDANCE_CHOICES = (
        ('absent','Absent'),
        ('present','Present'),
    )
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    attendanceReq_id = models.ForeignKey(AttendanceReq,on_delete=models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=ATTENDANCE_CHOICES,max_length=10,default='present')

    def __str__(self):
        return f'{self.student} {self.status} in {self.date_time.time().strftime("%H:%M:%S")}'

