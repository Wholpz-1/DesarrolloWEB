
from django.db import models



class Cliente(models.Model):
    CodigoCliente = models.AutoField(primary_key=True)
    NombreCliente = models.CharField(max_length=75)
    Direccion = models.CharField(max_length=75)
    Telefono = models.CharField(max_length=12)

    def __str__(self):
        return '{}'.format(self.NombreCliente)