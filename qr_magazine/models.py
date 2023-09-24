from django.db import models

# Create your models here.
class QR_base(models.Model):
    title = models.CharField(max_length=250)
    qrcode = models.ImageField(upload_to='qr_magazine/qr_base/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title