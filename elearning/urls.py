from django.contrib import admin
from django.urls import path,include
from django.views.i18n import JavaScriptCatalog
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    path('user/',include('users.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)