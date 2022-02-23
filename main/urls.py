from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('',Main,name='main'),
    path('my/',HomeView.as_view(),name='homey'),
    path('my/course-<int:pk>',DetailEdit.as_view(),name='detail_course'),
    path('my/course-<int:id>/attendance-<int:pk>',DetailAttend.as_view(),name='detail_attend'),
    path('add-course/',AddCourse.as_view(template_name='main/add_course.html'),name='add-course')
]