from django.db import models

from Models.Cliente.models import Cliente
from Models.Empleado.models import Empleado
from Models.TipoProyecto.models import TipoProyecto


class proyect(models.Model):
    CodigoProyecto = models.AutoField(primary_key=True)
    NombreProyecto = models.CharField(max_length=75)
    empleado_CodigoEmpleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    tipopro_CodigoTipoPro = models.ForeignKey(TipoProyecto, on_delete=models.CASCADE)
    cliente_CodigoCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    FechaInicio = models.DateField()
    FechaEntrega = models.DateField()

    def __str__(self):
        return '{}'.format(self.NombreProyecto)