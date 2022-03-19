from main import forms
from .models import *
from django.http import HttpResponseNotFound,Http404
from django.shortcuts import render
from django.utils import timezone

def Context_Std(user,**kwargs):
    context = {}
    student = Student.objects.get(user=user)
    classroom = Classroom.objects.get(name=student.class_id)
    courses = Course.objects.filter(class_id=classroom)
    context = {'classroom':classroom,'courses':courses}
    if len(kwargs) > 0:
        object = kwargs['object']
        attendance_req = AttendanceReq.objects.filter(course_id=object)
        context['attendance_req_list'] = attendance_req
    return context

def Context_Tcr(user,**kwargs):
    context = {}
    teacher = Teacher.objects.get(user=user)
    courses = Course.objects.filter(teacher_id=teacher)
    context = {'teacher':teacher,'courses':courses}
    if len(kwargs) > 0:
        object = kwargs['object']
        attendance_req = AttendanceReq.objects.filter(course_id=object)
        context['attendance_req_list'] = attendance_req

    return context

def check_expd_absent(object):
    if object == "all":
        attendance_req = AttendanceReq.objects.all()
    else:
        attendance_req = AttendanceReq.objects.filter(course_id=object)

    for request in attendance_req:
        closed_time = request.closed_time
        noww = timezone.now()
        if noww.date() == closed_time.date():
            if noww.time() >= closed_time.time():
                request.is_closed = True
        else:
            request.is_closed = True
        request.save()

def make_attendance(student,attreq_id,status):
    att_create = Attendance.objects.create(student=student,attendanceReq_id=attreq_id,status=status)
    att_create.save()

def check_no_double_attend(object,request):
    student = Student.objects.get(user=request.user)
    attendance = Attendance.objects
    list_attend = attendance.filter(student=student,attendanceReq_id=object)

    context = {}
    if object.is_closed:
        context['expired'] = 'Sorry You are late'
        print(list_attend)
        if len(list_attend) > 1:
            leng_list   = len(list_attend) - 1
            list_attend[:leng_list].delete()

    else:
        if len(list_attend) == 1:
            context['expired'] = "Thx For Submitting"
            attendance.get(student=student,attendanceReq_id=object)

        elif len(list_attend) == 0:
            context['form1'] = forms.MakeAbsent
            
        else:
            leng_list   = len(list_attend) - 1
            print(leng_list)
            list_attend[:leng_list].delete()    
            print(attendance.filter(student=student,attendanceReq_id=object))
    return context
    