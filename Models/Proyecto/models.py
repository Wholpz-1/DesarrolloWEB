
from django.db import models

from Models.Empleado.models import Empleado
from Models.TipoProyecto.models import TipoProyecto


class Proyecto(models.Model):
    CodigoProyecto = models.AutoField(primary_key=True)
    NombreProyecto = models.CharField(max_length=75)
    empleado_CodigoEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    tipopro_CodigoTipoPro = models.ForeignKey(TipoProyecto, on_delete=models.CASCADE)
    Personal = models.CharField(max_length=12)
    Presupuesto = models.CharField(max_length=20)
    Maquinas = models.CharField(max_length=75)
    ContracionServicios = models.CharField(max_length= 75)
    FechaInicio = models.DateField()
    FechaEntrega = models.DateField()
