from django.db import models

from Models.Empleado.models import Empleado


class Proyecto(models.Model):
    CodigoProyecto = models.AutoField(primary_key=True)
    NombreProyecto = models.CharField(max_length=75)
    empleado_CodigoEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
