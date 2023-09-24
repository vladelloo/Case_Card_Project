from django.shortcuts import render, get_object_or_404

from qr_magazine.models import QR_base

def magazine(request):
    qrcode = QR_base.objects.all()[:5]
    return render(request,'qr_magazine/magazine.html', {'base': qrcode})

def detail(request, qrcode_id):
    qrcode = get_object_or_404(QR_base, pk=qrcode_id)
    return render(request,'qr_magazine/detail.html', {'qrcode': qrcode})