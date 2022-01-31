from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import *

# from django.contrib.auth.models
# Register your models here.

class CustUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Halooo', {
                'fields': (
                    'user_type',
                ),
            }
        ),
    )
    
admin.site.register(CustomUser, CustUserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Classroom)
admin.site.register(Course)
admin.site.register(Attendance)
admin.site.register(AttendanceReq)

