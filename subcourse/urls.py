from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required


name_app = 'subcourse'
urlpatterns = [

    path('my/section-<int:pk>-edit',SectionEdit.as_view(),name='section_edit'),
    path('my/course-<int:id>/<slug:slug>',SubCourseView.as_view(),name='sub_course'),
]