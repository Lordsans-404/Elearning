from tracemalloc import start
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
        context['sub_courses'] = SubCourse.objects.filter(course_id=object)
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
        section_list = SubSection.objects.filter(course_id=object)
        section_course = {}
        for section in section_list:
            subcourse = SubCourse.objects.filter(subsection_id=section.pk)
            section_course[section] = subcourse
        context['section_course'] = section_course
        print(section_course)
    return context

def check_expd_absent(object):
    if object == "all":
        attendance_req = AttendanceReq.objects.all()
    else:
        attendance_req = AttendanceReq.objects.filter(course_id=object)

    for request in attendance_req:
        closed_time = request.closed_time
        start_time = request.start_time
        noww = timezone.now()
        if request.is_closed == False: #if request is not closed
            if noww.date() == start_time.date(): #if noww(date) is same as start_time(date)
                if noww.time() <= start_time.time(): #if noww(time) less than start_time(time)
                    request.is_closed = True # close the request
                

            elif noww.date() == closed_time.date(): #(else) if, now same as closed_time(date)
                if noww.time() >= closed_time.time(): #if now, is more than the closed_time
                    request.is_closed = True # close the request
            
            else: # if the now(date) is not same as the start and closed time(date)
                request.is_closed = True
        else: # if request is closed
            if noww.date() == start_time.date(): # if start_time same as now
                if noww.time() > start_time.time(): # if now has passing the start_time 
                    print('yeeey')
                    request.is_closed = False# open the request

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
        print(len(list_attend),'oy')
        if len(list_attend) == 1:
            context['expired'] = "Thx For Submitting"
            attendance.get(student=student,attendanceReq_id=object)

        elif len(list_attend) == 0:
            context['form1'] = forms.MakeAbsent
            
        else:
            leng_list   = len(list_attend) - 1
            for attend in list_attend[:leng_list]:
                print(attend)
                attend.delete()
                
            
    return context
    