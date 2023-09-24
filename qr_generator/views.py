from django.shortcuts import render
from django.http import HttpResponse
import hashlib

# Create your views here.

def home(request):
    return render(request, 'qr_generator/home.html')

def qr_code(request):

    open_key = list(request.GET.get('open key'))

    if request.GET.get('tourniquet'):
        open_key.extend(str('tourniquet'))
    if request.GET.get('anesthesia'):
        open_key.extend(str('anesthesia'))
    if request.GET.get('antibiotic'):
        open_key.extend(str('antibiotic'))
    if request.GET.get('tranexamic acid'):
        open_key.extend(str('tranexamic acid'))
    if request.GET.get('antiemetic'):
        open_key.extend(str('antiemetic'))
    if request.GET.get('immobilization'):
        open_key.extend(str('immobilization'))

    qr_list = []
    for i in open_key:
        qr_list += [i.encode()]

    hash_dabl = []
    for i in qr_list:
        hash_dabl += [hashlib.sha256(i).hexdigest()]

    hash_dabl = "".join(hash_dabl)

    qrcode = hashlib.sha256((hash_dabl).encode()).hexdigest()

    return render(request, 'qr_generator/qr_code.html', {'qrcode': qrcode})
