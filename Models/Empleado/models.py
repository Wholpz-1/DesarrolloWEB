from django.db import models

class Empleado(models.Model):
    CodigoEmpleado = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=75)
    Apellido = models.CharField(max_length=75)
    Telefono = models.CharField(max_length=12)
    DPI = models.CharField(max_length=20)
    Direccion = models.CharField(max_length=75)

    def __str__(self):
        return '{} {}'.format(self.Nombre, self.Apellido)