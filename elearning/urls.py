from django.contrib import admin
from django.urls import path,include
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    path('user/',include('users.urls')),
]
