from django.forms import ModelForm

from Models.Empleado.models import Empleado


class FormularioEmpleado(ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'

