from django.forms import ModelForm

from Models.TipoProyecto.models import TipoProyecto

class FormularioTipoPro(ModelForm):
    class Meta:
        model = TipoProyecto
        fields = '__all__'
