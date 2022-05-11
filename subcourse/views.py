from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.urls import reverse,reverse_lazy
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound,Http404
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import ModelFormMixin
from main import views as mainview
from main import models as main
from . import models,forms

# Create your views here.

class SubCourseView(LoginRequiredMixin,DetailView):
    template_name = 'subcourse/subcourse.html'
    model = models.SubCourse

class SectionEdit(LoginRequiredMixin,View,SingleObjectMixin):
    template_name = 'subcourse/section_edit.html'
    model = models.SubSection
    form1 = forms.AddSection
    form2 = forms.AddSubCourse
    
    def post(self,request,**kwargs):
        obj = self.get_object()
        if request.user.user_type == 'Tcr':
            form1 = self.form1(request.POST,instance=obj)#needs instance for edit object
            form2 = self.form2(request.POST)
            print('hmmm')
            if form1.is_valid():
                form1.save()
            if form2.is_valid():
                crs_id      = obj.course_id
                sect_id     = obj
                name        = form2.cleaned_data['name']
                content1    = form2.cleaned_data['content1']
                content2    = form2.cleaned_data['content2']
                sub_crs     = models.SubCourse.objects.create(course_id=crs_id,subsection_id=sect_id,
                    name=name,content1=content1,content2=content2
                )
                print(sub_crs)
                sub_crs.save()
            return redirect('courses_page', obj.course_id.pk)

        else:
            raise Http404
        
    def get(self,request,**kwargs):
        self.object = self.get_object()
        self.extra_context = {'form1':self.form1(instance=self.object),'form2':self.form2}
        context = self.get_context_data()
        if request.user.user_type == 'Tcr' or request.user.user_type == 'Adm':# if user is admin or user is a teacher
            return render(request,self.template_name,context)
        else:# if user is a student
            raise Http404


class DetailAssignment(LoginRequiredMixin,DetailView):
    model = models.Assignment
    template_name = 'subcourse/subcourse.html'
