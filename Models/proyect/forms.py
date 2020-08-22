from django.forms import ModelForm
from django.forms import DateInput

from Models.proyect.models import proyect


class FormularioProyecto(ModelForm):
    class Meta:
        model = proyect
        fields = [

            'NombreProyecto',
            'empleado_CodigoEmpleado',
            'tipopro_CodigoTipoPro',
            'cliente_CodigoCliente',
            'FechaInicio',
            'FechaEntrega',


        ]

        labels = {

            'empleado_CodigoEmpleado': 'Nombre del Lider de Proyecto',
            'tipopro_CodigoTipoPro': 'Tipo de Proyecto',
            'cliente_CodigoCliente' : 'Cliente',
            'FechaInicio' :  'Fecha de Inicio ',
            'FechaEntrega': 'Fecha de Entrega',
        }

        widgets = {'FechaEntrega': DateInput(attrs={'type': 'date'}),'FechaInicio': DateInput(attrs={'type':'date'})}
