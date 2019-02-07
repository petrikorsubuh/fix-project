from django.db import models

# Create your models here.
 class Building(models.Model):
     nama =models.CharField(max_length=100)

     def __str__(self):
         return self.nama

class Rooms(models.Model):
    nama =models.CharField(max_length=100)
    building = models.ForeignKey(Building,on_delete=models.CASCADE)

    def __str__(self):
        return self.nama