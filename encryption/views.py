from django.shortcuts import render
import base64
from encryptor_decryptor.Encrypter import Encrypter
from encryptor_decryptor.Decrypter import Decrypter
import os
from pathlib import Path

# Create your views here.
def index(request):
    return render(request, 'enc/index.html')

def encrypt(request):
    if (request.method == "POST"):
        image = request.FILES['image']
        stri = ""
        stri = base64.b64encode(image.read())
        key = request.POST['key']
        x = Encrypter(stri, key)
        cipher = x.encrypt_image()
        # path = "static/ima"
        # file_name = 'cipher_web.txt'
        # completeName = os.path.join(path, file_name)
        # fh = open('cipher_web.txt', "wb")
        # fh.write(cipher)
        # fh.close()
        # print(type(cipher))
        text = cipher.decode('utf-8')
        return render(request, 'enc/cipher_file_download.html', {'cipher': text})