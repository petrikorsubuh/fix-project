from django.db import models

from apps.kecamatan.models import Kecamatan
class Kelurahan(models.Model):
    kecamatan = models.ForeignKey(Kecamatan,on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama