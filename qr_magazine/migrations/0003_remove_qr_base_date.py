# Generated by Django 4.2.5 on 2023-09-22 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qr_magazine', '0002_qr_base_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qr_base',
            name='date',
        ),
    ]
