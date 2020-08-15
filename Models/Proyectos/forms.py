from django.forms import ModelForm

from Models.Proyectos.models import Proyecto

class FormularioProyecto(ModelForm):
    class Meta:
        model = Proyecto
        fields = [

            'NombreProyecto',
            'empleado_CodigoEmpleado',


        ]
        labels = {

            'empleado_CodigoEmpleado' : 'Nombre del Lider de Proyecto',


        }