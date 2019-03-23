from django.db import models

# Create your models here.
# dapil
class Dapil(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
