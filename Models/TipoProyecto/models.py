from django.db import models


class TipoProyecto(models.Model):
    CodigoTipoPro = models.AutoField(primary_key=True)
    Descripcion = models.CharField(max_length=75)

    def __str__(self):
        return '{}'.format(self.Descripcion)

