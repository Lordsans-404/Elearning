from django.shortcuts import redirect, render
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from . import forms
from django.urls import reverse,reverse_lazy
from django.views.generic import *
from . import utils
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound,Http404
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import ModelFormMixin


# Create your views here.
def Main(request):
    model = Student.objects.all()
    utils.check_expd_absent("all")
    context = {
        'student':model
    }
    return render(request,'main/main.html',context)


class HomeView(LoginRequiredMixin,TemplateView):# this view for homey
    model = Classroom
    
    def get_context_data(self,*args,**kwargs):
        request = self.request
        context =  super().get_context_data(**kwargs) 
        user = request.user
        if user.is_authenticated:
            if user.user_type == 'Std':
                context.update(utils.Context_Std(user))

            elif user.user_type == 'Tcr':
                context.update(utils.Context_Tcr(user))
                context['tcr_or_not'] = 'hola'

        self.template_name = 'main/home.html'
        return context

class DetailEdit(LoginRequiredMixin,SingleObjectMixin,View):# this view for courses_page
    template_name = 'main/detail_crse.html'
    model = Course
    form1 = forms.AddAttendanceReq

    def post(self,request,**kwargs):
        print(request.user.user_type)
        if request.user.user_type == 'Tcr':
            form = self.form1(request.POST)
            if form.is_valid():
                print('hey')
                course = self.get_object()
                start = form.cleaned_data['start_time']
                closed = form.cleaned_data['closed_time']
                is_closed = form.cleaned_data['is_closed']
                att_req = AttendanceReq.objects.create(course_id=course,start_time=start,closed_time=closed,is_closed=is_closed)
                att_req.save()

            return redirect('homey')

    def get(self,request,**kwargs):
        context = {}
        user = request.user
        object = self.get_object()
        context['course'] = object
        returnee = {'object':object,'form1':self.form1}
        utils.check_expd_absent(object)
        if user.is_authenticated:

            if user.user_type == 'Std':
                context.update(utils.Context_Std(user,**returnee))
                if object.class_id == context['classroom']:
                    return render(request,'main/detail_crse.html',context)
                else:
                    raise Http404

            elif user.user_type == 'Tcr' :
                context['form1'] = self.form1
                context.update(utils.Context_Tcr(user,**returnee))
                if object.teacher_id == context['teacher']:
                    return render(request,'main/detail_crse.html',context)
                else:
                    raise Http404

            else:
                raise Http404
        
class DetailAttend(LoginRequiredMixin,SingleObjectMixin,View):# this view for detail_attend
    model = AttendanceReq
    template_name = 'main/det_attend.html'
    form1 = forms.MakeAbsent


    def post(self,request,**kwargs):
        if request.user.user_type == 'Std':
            form = self.form1(request.POST)
            if form.is_valid():
                student = Student.objects.get(user=request.user)
                attreq_id = AttendanceReq.objects.get(id=kwargs['pk'])
                utils.make_attendance(student,attreq_id,form.cleaned_data['status'])
            return redirect('courses_page', kwargs['id'])

    def get(self,request,**kwargs):
        object = self.get_object()
        context = {}
        user = request.user
        if user.is_authenticated:
            context['object'] = object
            if user.user_type == 'Std':
                context.update(utils.check_no_double_attend(object,request))
            
            elif user.user_type == 'Tcr':
                list_attendance = Attendance.objects.filter(attendanceReq_id=object)
                context['list_attend'] = list_attendance
                context['tcr_true'] = True
            return render(request,self.template_name,context)

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

