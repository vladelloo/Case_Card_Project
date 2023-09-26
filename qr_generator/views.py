import qrcode
from django.shortcuts import render
from django.http import HttpResponse
import hashlib

# Create your views here.

def home(request):
    return render(request, 'qr_generator/home.html')

def qr_code(request):

    names_list = ['nickname', 'birthday', 'personalNumber', 'subdivision', 'diagnosis', 'tourniquet',
                  'anesthesia', 'allergy', 'note', 'infuzion', 'shock', 'blood', 'bloodRh', 'ultrasound', 'xRay', 'sorting']

    description = request.GET.get('firstName')
    description = [description + request.GET.get(name) for name in names_list if request.GET.get(name)]

    qr_list = []
    for i in description:
        qr_list += [i.encode()]

    hash_dabl = []
    for i in qr_list:
        hash_dabl += [hashlib.sha256(i).hexdigest()]

    hash_dabl = "".join(hash_dabl)

    data = hashlib.sha256((hash_dabl).encode()).hexdigest()
    qrcode_img = qrcode.make(data)
    qrcode_img.save(f'D:/Case_Card/media/qr_magazine/qr_base/{hash_dabl[:5]}.jpg')
    img_address = str(f'D:/Case_Card/media/qr_magazine/qr_base/{hash_dabl[:5]}.jpg')

    return render(request, 'qr_generator/qr_code.html', {'qrcode': img_address})
