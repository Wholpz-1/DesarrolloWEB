from django.forms import ModelForm
from django.forms import DateInput

from Models.Proyecto.models import Proyecto


class FormularioProyect(ModelForm):
    class Meta:
        model = Proyecto
        fields = [

            'NombreProyecto',
            'empleado_CodigoEmpleado',
            'tipopro_CodigoTipoPro',
            'Personal',
            'Presupuesto',
            'Maquinas',
            'ContracionServicios',
            'FechaInicio',
            'FechaEntrega',


        ]

        labels = {

            'empleado_CodigoEmpleado': 'Nombre del Lider de Proyecto',
            'tipopro_CodigoTipoPro': 'Tipo de Proyecto',
            'ContracionServicios' : 'Contratacion de Servicios',
            'FechaInicio' :  'Fecha de Inicio ',
            'FechaEntrega': 'Fecha de Entrega',
            'Maquinas' : 'Equipo a Utilizar',
        }

        widgets = {'FechaEntrega': DateInput(attrs={'type': 'date'}),'FechaInicio': DateInput(attrs={'type':'date'})}
