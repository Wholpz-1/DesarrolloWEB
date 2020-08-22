from django.db import models

from Models.proyect.models import proyect


class RecursosPro(models.Model):
    CodigoRecursos = models.AutoField(primary_key=True)
    proyecto_CodigoProyecto = models.ForeignKey(proyect, on_delete=models.CASCADE)
    Personal = models.CharField(max_length=20)
    Presupuesto = models.CharField(max_length=20)
    Maquinas = models.CharField(max_length=75)
    ContracionServicios = models.CharField(max_length=75)

