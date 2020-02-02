from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('task3.urls')),
    path('task3/',include('task3.urls')),
    path(r'media/(?P<path>.*)', serve,{'document_root': settings.MEDIA_ROOT}),
    path(r'static/(?P<path>.*)', serve,{'document_root': settings.STATIC_ROOT})

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
