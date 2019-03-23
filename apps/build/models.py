from django.db import models
from apps.dapil.models import Dapil

# Create your models here.


class Building(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama


class Rooms(models.Model):
    nama = models.CharField(max_length=100)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama


class Kategori(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama


class Item(models.Model):
    nama = models.CharField(max_length=100)
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama


class Language(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Framework(models.Model):
    name = models.CharField(max_length=100)
    release = models.DateField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.name










