from audioop import add
from multiprocessing import context
from main import forms
from .models import *
from django.http import HttpResponseNotFound,Http404
from django.shortcuts import render


def Context_Std(user):
    student = Student.objects.get(user=user)
    classroom = Classroom.objects.get(name=student.class_id)
    courses = Course.objects.filter(class_id=classroom)
    return {'courses':courses,}

def Context_Tcr(user):
    teacher = Teacher.objects.get(user=user)
    courses = Course.objects.filter(teacher_id=teacher)
    return {'courses':courses}

def DetailEdit_std(request,object,context):
    student =   Student.objects.get(user=request.user)
    classroom = Classroom.objects.get(name=student.class_id)
    course = object
    if course.class_id == classroom:
        return render(request,'main/detail_crse.html',context)
    else:
        raise Http404

def DetailEdit_tcr(request,object,context):
    teacher = Teacher.objects.get(user=request.user)
    course = object
    attendance_req = AttendanceReq.objects.all()
    context['attendance_req_list'] = attendance_req
    if course.teacher_id == teacher:
        return render(request,'main/detail_crse.html',context)
    else:
        raise Http404


def check_expd_absent(request):
    pass