
from django.db import models

from Models.Proyecto.models import Proyecto



class Cliente(models.Model):
    CodigoCliente = models.AutoField(primary_key=True)
    NombreCliente = models.CharField(max_length=75)
    Direccion = models.CharField(max_length=75)
    Telefono = models.CharField(max_length=12)

