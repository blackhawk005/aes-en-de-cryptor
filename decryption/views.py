from django.shortcuts import render
import base64
from encryptor_decryptor.Encrypter import Encrypter
from encryptor_decryptor.Decrypter import Decrypter
import os
from pathlib import Path
import io
import PIL.Image as Image
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'dec/index.html')

def wrong_key(request):
    return render(request, 'dec/wrong_key.html')

def decrypt(request):
    # print(request.POST, request.FILES)
    try:
        print(request.FILES['txt_file'])
        txt = request.FILES['txt_file']
        text=txt.read()
        cipher= text.decode('utf-8')
        key = request.POST['key']
        x = Decrypter(cipher)
        byte=x.decrypt_image(key)
        images = Image.open(io.BytesIO(byte))
        buffered = io.BytesIO()
        images.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue())
        print(img_str.decode('utf-8'))
        # img_byte_arr = io.BytesIO()
        # images.save(img_byte_arr, format='PNG')
        # img_byte_arr = img_byte_arr.getvalue()
        # converted_bytes = base64.b64encode(img_byte_arr)
        # converted_string = converted_bytes.decode('utf-8')

        return render(request, 'dec/image_download.html', {'byte': img_str})
    except:
        return render(request, 'dec/wrong_key.html')
