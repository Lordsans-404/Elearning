
# def all_in_one(template,user,request,**kwargs):
#     if user.is_authenticated:
#         context = {}

#         if user.user_type == 'Std':
#             try:
#                 student     = Student.objects.get(user=user)
#                 classroom   = Classroom.objects.get(name=student.class_id)
#                 courses     = Course.objects.filter(class_id=classroom)
#                 context     = {'classroom':classroom,'courses':courses}
#                 if len(kwargs) > 0:
#                     object = kwargs['object']
#                     attendance_req = AttendanceReq.objects.filter(course_id=object)
#                     context['attendance_req_list'] = attendance_req
#                     if object.class_id == classroom:
#                         return render(request,template,context)
#                     else:
#                         raise Http404

#                 else:
#                     return render(request,template,context)

#             except:
#                 raise Http404

#         elif user.user_type == 'Tcr':
#             try:
#                 teacher = Teacher.objects.get(user=user)
#                 courses = Course.objects.filter(teacher_id=teacher)
#                 context = {'courses':courses}
#                 if len(kwargs) > 0:
#                     object = kwargs['object']
#                     attendance_req = AttendanceReq.objects.filter(course_id=object)
#                     context['attendance_req_list'] = attendance_req
#                     context['form1'] = kwargs['form1']

#                     if object.teacher_id == teacher: 
#                         return render(request,'main/detail_crse.html',context)
                   
#                     else:
#                         raise Http404
#             except:
#                 raise Http404
#             return render(request,template,context)
        
#         else:
#             raise Http404

