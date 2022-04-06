from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models
from django.contrib.admin.widgets import AdminSplitDateTime,AdminTimeWidget


class AddSubCourse(forms.ModelForm):
    class Meta:
        model = models.SubCourse
        exclude = ['course_id','subsection_id','slug']

class AddSection(forms.ModelForm):
    class Meta:
        model = models.SubSection
        fields = ['title']        
