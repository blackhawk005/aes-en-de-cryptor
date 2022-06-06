from django.urls import path
from .views import *
from django.urls.conf import include

app_name = "decryption"

urlpatterns = [
    path('', index, name='decryption_index'),
    path('decrypt/', decrypt, name='decrypt_image'),
    path('wrong_key/', wrong_key, name='wrong_key')
]