from django.urls import path
from .views import *
from django.urls.conf import include

urlpatterns = [
    path('', index, name='index')
]