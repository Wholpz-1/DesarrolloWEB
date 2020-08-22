from django.forms import ModelForm


from Models.RecursosPro.models import RecursosPro


class FormularioRecursosPro(ModelForm):
    class Meta:
        model = RecursosPro
        fields = [

            'proyecto_CodigoProyecto',
            'Personal',
            'Presupuesto',
            'Maquinas',
            'ContracionServicios',

        ]

        labels = {

            'empleado_CodigoEmpleado': 'Nombre del Lider de Proyecto',
            'ContracionServicios' : 'Contratacion de Servicios',
            'Maquinas' : 'Equipo a Utilizar',
        }


