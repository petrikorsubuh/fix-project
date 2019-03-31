from django.db import models

from apps.dapil.models import Dapil
from apps.caleg.models import Caleg
from apps.tps.models import  Tps

# Create your models here.
class Suara(models.Model):
    jumlah_suara = models.IntegerField()
    pict = models.ImageField(upload_to='upload_pict/')


    def __str__(self):
        return f'{self.caleg} -> {self.jumlah_suara}'