from django.db import models


class Partai(models.Model):
    name = models.CharField(max_length=100)
    no_urut = models.IntegerField(null=True, blank=True)
    gambar = models.ImageField(upload_to='upload_pict/', null=True, blank=True)

    def __str__(self):
        return self.name
