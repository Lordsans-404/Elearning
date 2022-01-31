from multiprocessing import context
from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from . import forms
from django.urls import reverse
from django.views.generic import *
from . import utils
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound,Http404
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import ModelFormMixin


# Create your views here.
def Main(request):
    model = Student.objects.all()
    context = {
        'student':model
    }
    return render(request,'main/main.html',context)


class HomeView(LoginRequiredMixin,TemplateView):
    model = Classroom
    
    def get_context_data(self,*args,**kwargs):
        request = self.request
        context =  super().get_context_data(**kwargs) 
        user = request.user
        tcr_or_not = None
        if user.is_authenticated:
            if user.user_type == 'Std':
                context.update(utils.Contex_tStd(user))
                tcr_or_not = False

            elif user.user_type == 'Adm':
                tcr_or_not = False

            else :
                context.update(utils.Context_Tcr(user))
                tcr_or_not = True
        context['tcr_or_not'] = tcr_or_not
        self.template_name = 'main/home.html'
        return context

class DetailEdit(LoginRequiredMixin,SingleObjectMixin,View):
    template_name = 'main/detail_crse.html'
    model = Course
    form1 = forms.AddAttendanceReq

    def get(self,request,**kwargs):
        context = {}
        user = request.user
        tcr_or_not = None
        object = self.get_object()
        context['course'] = object
        if user.is_authenticated:
            if user.user_type == 'Std':
                return utils.DetailEdit_std(request,object,context)

            else :
                context['form1'] = self.form1
                return utils.DetailEdit_tcr(request,object,context)


        

class AddCourse(LoginRequiredMixin,CreateView):
    model = Course
    form_class = forms.AddNewCourse
    succes_url = '/'

    def form_valid(self, form):
        user = self.request.user
        teacher = Teacher.objects.get(user=user)
        form.instance.teacher_id = teacher
        # mengisi bagian teacher_id secara otomatis
        return super().form_valid(form)

