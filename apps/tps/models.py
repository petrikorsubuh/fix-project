from django.db import models

# Create your models here.
class Tps(models.Model):
    kecamatan = models.CharField(max_length=100,blank=True,null=True)
    kelurahan = models.CharField(max_length=100,blank=True,null=True)
    address = models.CharField(max_length=100,blank=True,null=True)
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['kecamatan']