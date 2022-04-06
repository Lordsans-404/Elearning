import imp
from django.db import models
from main import models as main
# Create your models here.

class SubSection(models.Model):
    course_id = models.ForeignKey(main.Course,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.title}-{self.course_id.name}"

class SubCourse(models.Model):
    course_id = models.ForeignKey(main.Course,on_delete=models.CASCADE,null=True)
    subsection_id = models.ForeignKey(SubSection,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200)
    content1 = models.CharField(max_length=255)
    content2 = models.CharField(max_length=255,null=True,blank=True)
    slug = models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.name
    
    @property
    def get_slug(self):
        if self.slug == None:
            self.slug = main.slugify(self.name)
            super(SubCourse,self).save()
        return self.slug

