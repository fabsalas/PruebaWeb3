from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import base, cpu, gpu, hdd, m2, mb, psu, ram, sdd, signin, hardware

urlpatterns = [
    path('', base, name = 'base'),
    path('signin', signin, name = 'signin'),
    path('hardware', hardware, name = 'hardware'),
    path('mb', mb, name='mb'),
    path('cpu', cpu, name='cpu'),
    path('gpu', gpu, name='gpu'),
    path('psu', psu, name='psu'),
    path('ram', ram, name='ram'),
    path('hdd', hdd, name='hdd'),
    path('sdd', sdd, name='sdd'),
    path('m2', m2, name='m2')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)