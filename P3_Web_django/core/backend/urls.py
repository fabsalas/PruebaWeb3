from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import base, signin, signup, hardware

urlpatterns = [
    path('', base, name = 'base'),
    path('signin', signin, name = 'signin'),
    path('signup', signup, name = 'signup'),
    path('hardware', hardware, name = 'hardware')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)