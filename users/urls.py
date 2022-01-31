from django.urls import path
from .views import *

urlpatterns = [
    path('login/',loginPage,name='login'),
    path('logout/',logoutPage,name='logout'),
    path('register/',registerPage,name='signup'),
    path('fail/',failPage,name='fail')
]