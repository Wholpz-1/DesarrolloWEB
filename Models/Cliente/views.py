from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from xhtml2pdf import pisa

from Models.Cliente.forms import FormularioCliente
from Models.Cliente.models import Cliente


class FormularioClienteView(HttpRequest):
    def index(request):
        cliente = FormularioCliente()
        return render(request, "ClienteIndex.html", {"form":cliente})

    def procesar_formulario(request):
        cliente = FormularioCliente(request.POST)
        if cliente.is_valid():
            cliente.save()
            cliente = FormularioCliente()

            return render(request, "ClienteIndex.html", {"form":cliente, "mensaje": 'ok'})

    def listar_Cliente(request):
        cliente = Cliente.objects.all()
        return render(request, "ListaCliente.html", {"clientes":cliente})

    def eliminarCliente(request,id):
        Cliente.objects.filter(CodigoCliente=id).delete()
        return redirect(to="listarCliente")

    def editarCliente(request, id):
        actua= Cliente.objects.get(CodigoEmpleado=id)
        data = {
            'form': FormularioCliente(instance=actua)
        }
        if request.method == 'POST':
            formulario = FormularioCliente(data=request.POST, instance=actua)
            if formulario.is_valid():
                formulario.save()
                data['mensaje']= "Se Actualizo el Registro."
                data['form']=formulario

        return render(request, 'modificarCliente.html',data)

    def ReportPDF(self, *args, **kwargs):

        template = get_template('ReportePDF3.html')
        context = {'report': Cliente.objects.all(),
                   'comp': {'name': 'Reporte de Cliente'}
                   }
        html = template.render(context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        pisaStatus = pisa.CreatePDF(

            html, dest=response)

        if pisaStatus.err:
            return HttpResponse('we had some errors <pre>' + html + '</pre>')

        return response




