from django.db import models
from apps.kelurahan.models import Kelurahan

# Create your models here.
class Tps(models.Model):
    kelurahan = models.ForeignKey(Kelurahan,on_delete=models.CASCADE)
    alamat = models.CharField(max_length=100,blank=True,null=True)
    nama = models.CharField(max_length=100)
    

    def __str__(self):
        return self.nama
    
    class Meta:
        ordering = ['nama','alamat']