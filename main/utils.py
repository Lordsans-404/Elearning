from audioop import add
from multiprocessing import context
from main import forms
from .models import *
from django.http import HttpResponseNotFound,Http404
from django.shortcuts import render
from datetime import datetime


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
    attendance_req = AttendanceReq.objects.filter(course_id=course)
    context['attendance_req_list'] = attendance_req
    if course.teacher_id == teacher:
        return render(request,'main/detail_crse.html',context)
    else:
        raise Http404


def check_expd_absent(object):
    attendance_req = AttendanceReq.objects.filter(course_id=object)
    for request in attendance_req:
        start_time = request.start_time.time()
        closed_time = request.closed_time.time()
        now = datetime.date.today()
        if now.time > closed_time:
            print('uhuy')
    pass


