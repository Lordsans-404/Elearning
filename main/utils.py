import imp
import itertools
from main import forms
from .models import *
from django.http import HttpResponseNotFound,Http404
from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseNotFound,Http404,JsonResponse
from django.core import serializers
from subcourse import models
from itertools import chain
from operator import attrgetter

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
        section_list = models.SubSection.objects.filter(course_id=object)
        section_course = {}
        for section in section_list:
            subcourse = models.SubCourse.objects.filter(sub_id=section.pk)
            assignment = models.Assignment.objects.filter(sub_id=section.pk)
            section_course[section] = sorted(itertools.chain(subcourse,assignment),key=attrgetter('date_time'))
        context['section_course'] = section_course
        
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
        section_list = models.SubSection.objects.filter(course_id=object)
        section_course = {}
        for section in section_list:
            subcourse = models.SubCourse.objects.filter(sub_id=section.pk)
            assignment = models.Assignment.objects.filter(sub_id=section.pk)
            section_course[section] = sorted(itertools.chain(subcourse,assignment),key=attrgetter('date_time'))
            # sorted subcourse and assignment by date_time

        context['section_course'] = section_course
    return context

        # for section in section_list:
        #     subcourse = models.SubCourse.objects.filter(sub_id=section.pk)
        #     assignment = models.Assignment.objects.filter(sub_id=section.pk)
        #     marbles = []
        #     for x,y in zip(subcourse,assignment):
        #         marbles.append(x)
        #         marbles.append(y)
        #     section_course[section] = marbles
        # print(section_course)

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
                if noww.time() < start_time.time(): #if noww(time) less than start_time(time)
                    request.is_closed = True # close the request

            elif noww.date() == closed_time.date(): #(else) if, now same as closed_time(date)
                if noww.time() >= closed_time.time(): #if now, is more than the closed_time
                    request.is_closed = True # close the request
            
            elif noww.date() > closed_time.date(): # (else) if, now is more than closed_time(date)
                request.is_closed = True
        else: # if request is closed
            if noww.date() == start_time.date(): # if start_time same as now
                if noww.time() >= start_time.time(): # if now has passing the start_time 
                    print('yeeey')
                    request.is_closed = False# open the request
            elif noww.date() > start_time.date() and noww.date() < closed_time.date():
                request.is_closed = False

        request.save()

def make_attendance(student,attreq_id,status):
    att_create = Attendance.objects.create(student=student,attendanceReq_id=attreq_id,status=status)
    att_create.save()

def editSubsection(post,**kwargs):# for DetailCourse
    obj = models.SubSection.objects.get(pk=post['pk'])
    form = kwargs['form'](post,instance=obj)
    if form.is_valid():
        instance = form.save()
        ser_instance = serializers.serialize('json', [ instance, ])
        return JsonResponse({"instance": ser_instance}, status=200)
    return JsonResponse({"error": "COK"}, status=400)

def ajaxPost(post,**kwargs):
    form = kwargs['form'](post)
    if form.is_valid():
        cleaned = form.cleaned_data
        if post['form-type'] == '3':
            instance = models.SubCourse.objects.create(
                course_id=Course.objects.get(pk=post['course_id']),
                sub_id=models.SubSection.objects.get(pk=post['sub_id']),
                name=cleaned['name'],
                content1=cleaned['content1'],
                content2=cleaned['content2']
            )
            instance.save()
            ser_instance = serializers.serialize('json', [ instance, ])
            return JsonResponse({'instance':ser_instance},status=200)
    return JsonResponse({"error": "COK"}, status=400)

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
    