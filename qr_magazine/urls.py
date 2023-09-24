from django.urls import path

from . import views
app_name = "qrcode"

urlpatterns = [
    path('', views.magazine, name='magazine'),
    path('<int:qrcode_id>/', views.detail, name='detail'),

]
