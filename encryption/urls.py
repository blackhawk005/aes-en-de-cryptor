from django.urls import path
from .views import *
from django.urls.conf import include

app_name = "encryption"

urlpatterns = [
    path('', index, name='encryption_index'),
    path('encrypt/', encrypt, name='encrypt_image')
]