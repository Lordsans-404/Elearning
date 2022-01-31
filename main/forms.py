from dataclasses import fields
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.contrib.admin.widgets import AdminSplitDateTime


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = models.CustomUser
        fields = '__all__'

class AddNewCourse(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = ['name','teacher_id','class_id']

class AddAttendanceReq(forms.ModelForm):
    class Meta:
        model = models.AttendanceReq
        fields = '__all__'
        widgets = {
            'start_time'     : AdminSplitDateTime(),
            'closed_time'    : AdminSplitDateTime(),
            'course_id'      : forms.TextInput(attrs={'class':'hidden'})
        }