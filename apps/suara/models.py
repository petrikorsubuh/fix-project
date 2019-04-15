from django.db import models

from apps.caleg.models import Caleg
from apps.tps.models import Tps
from apps.partai.models import Partai
from apps.kecamatan.models import Kecamatan
from apps.kelurahan.models import Kelurahan
# Create your models here.
class Suara(models.Model):
    caleg = models.ForeignKey(Caleg,on_delete=models.CASCADE,null=True)
    kecamatan = models.ForeignKey(Kecamatan,on_delete=models.CASCADE,null=True)
    kelurahan = models.ForeignKey(Kelurahan,on_delete=models.CASCADE,null=True)
    tps = models.ForeignKey(Tps,on_delete=models.CASCADE,null=True)
    jumlah_suara = models.IntegerField()
    pict = models.ImageField(upload_to='upload_pict/')
    create_add =models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.caleg} -> {self.jumlah_suara}'