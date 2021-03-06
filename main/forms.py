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
    start_time = forms.SplitDateTimeField(widget=forms.DateTimeInput(attrs={'class':'date-time'}))
    closed_time = forms.SplitDateTimeField(widget=forms.DateTimeInput(attrs={'class':'date-time'}))
    class Meta:
        model = models.AttendanceReq
        fields = ['is_closed']

class MakeAbsent(forms.ModelForm):
    class Meta:
        model = models.Attendance
        fields = ['status']
        widgets = {'status':forms.RadioSelect}