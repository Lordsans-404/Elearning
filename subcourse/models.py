from django.db import models
from main import models as main
from django.utils import timezone
import datetime
# Create your models here.

class SubSection(models.Model):
    course_id = models.ForeignKey(main.Course,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.pk}.{self.title}-{self.course_id.name}"

class SubCourse(models.Model):
    course_id = models.ForeignKey(main.Course,on_delete=models.CASCADE,null=True)
    sub_id = models.ForeignKey(SubSection,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=True, null=True)
    content1 = models.CharField(max_length=255)
    content2 = models.CharField(max_length=255,null=True,blank=True)
    slug = models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.name

    @property
    def get_slug(self):
        if self.slug == None:
            self.slug = main.slugify(self.name)
            self.slug += f"-{self.pk}"
            super(SubCourse,self).save()
        return self.slug

# class Activity(models.Model):
#     TYPE_CHOICES = {
#         'asgmt':'Assignment',
#         'rsc':'Resource',
#         'qz':'Quiz',
#     }
#     sub_id = models.ForeignKey(SubCourse,on_delete=models.CASCADE,null=True)
#     activity_type = models.CharField(choices=TYPE_CHOICES,default='asgmt',max_length=3)

class Assignment(models.Model):
    course_id = models.ForeignKey(main.Course,on_delete=models.CASCADE,null=True)
    sub_id = models.ForeignKey(SubSection,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    file = models.FileField(upload_to="uploads_file_tcr/",null=True,blank=True)
    date_time = models.DateTimeField(auto_now_add=True, null=True)
    start_time = models.DateTimeField()
    closed_time = models.DateTimeField()
    is_closed = models.BooleanField(default=False)
    slug = models.SlugField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.title}"
    
    @property
    def get_slug(self):
        if self.slug == None:
            self.slug = main.slugify(self.title)
            self.slug += f"-{self.pk}"
            super(Assignment,self).save()
        return self.slug

class StdAssignment(models.Model):
    student = models.ForeignKey(main.Student,on_delete=models.CASCADE)
    asgt_id = models.ForeignKey(Assignment,on_delete=models.CASCADE,null=True)
    date_time = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="uploads_file_std/")
    is_checked = models.BooleanField(blank=True,null=True)

    def __str__(self):
        return f"{self.asgt_id}{self.student}"

class UploadFile(models.Model):
    course_id = models.ForeignKey(main.Course,on_delete=models.CASCADE,null=True)
    sub_id = models.ForeignKey(SubSection,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255,null=True,blank=True)
    file = models.FileField(upload_to="uploads_file/")
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return f"{self.sub_id}{self.title}"

    @property
    def get_slug(self):
        if self.slug == None:
            self.slug = main.slugify(self.name)
            super(SubCourse,self).save()
        return self.slug