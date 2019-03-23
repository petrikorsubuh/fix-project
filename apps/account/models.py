from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Account(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='account')
    name = models.CharField(max_length=100)
    no_telpon = models.CharField(max_length=15)
    nik = models.CharField(max_length=20)
    gambar = models.ImageField(upload_to='upload_pict/',blank=True,null=True, default = 'path/static/img/default-user.png')
