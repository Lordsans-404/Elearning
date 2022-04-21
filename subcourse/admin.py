from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(SubCourse)
admin.site.register(SubSection)
admin.site.register(Assignment)
admin.site.register(StdAssignment)
admin.site.register(UploadFile)