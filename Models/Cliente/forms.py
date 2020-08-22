from django.forms import ModelForm

from Models.Cliente.models import Cliente


class FormularioCliente(ModelForm):
    class Meta:
        model = Cliente
        fields = [

            'NombreCliente',
            'Direccion',
            'Telefono',
        ]

        labels = {

            'NombreCliente': 'Nombre del Cliente',
            'Direccion': 'Direccion del Cliente',
            'Telefono': 'Telefono del Cliente',

        }

