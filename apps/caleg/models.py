from django.db import models

from apps.dapil.models import Dapil
from apps.partai.models import Partai
from apps.kategori.models import KategoriCaleg


# Create your models here.

class Caleg(models.Model):
    
    name =models.CharField(max_length=100)
    nomor_urut = models.IntegerField()
    dapil = models.ForeignKey(Dapil,on_delete=models.CASCADE, related_name='calegs')
    partai = models.ForeignKey(Partai,on_delete=models.CASCADE)
    kategoricaleg = models.ForeignKey(KategoriCaleg,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name
