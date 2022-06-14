from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.contrib.admin.widgets import AdminSplitDateTime,AdminTimeWidget


class AddSubCourse(forms.ModelForm):
    class Meta:
        model = models.SubCourse
        exclude = ['slug']

class AddSection(forms.ModelForm):
    class Meta:
        model = models.SubSection
        fields = ['title']        

class FormAssignmentTcr(forms.ModelForm):
    start_time = forms.SplitDateTimeField(widget=forms.DateTimeInput(attrs={'class':'date-time'}))
    closed_time = forms.SplitDateTimeField(widget=forms.DateTimeInput(attrs={'class':'date-time'}))
    class Meta:
        model = models.Assignment
        exclude = ["slug"]

