from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from xhtml2pdf import pisa

from Models.RecursosPro.forms import FormularioRecursosPro
from Models.RecursosPro.models import RecursosPro



class FormularioRecursosView(HttpRequest):

    def index(request):
        proyecto = FormularioRecursosPro()
        return render(request, "RecursosIndex.html", {"form": proyecto})

    def procesar_formulario(request):
        recurso = FormularioRecursosPro(request.POST)
        if recurso.is_valid():
            recurso.save()
            recurso = FormularioRecursosPro()

            return render(request, "RecursosIndex.html", {"form":recurso, "mensaje": 'ok'})

    def listar_Recursos(request):
        recurso = RecursosPro.objects.all()
        return render(request, "ListaRecursos.html", {"lb_recursos": recurso})

    def eliminarRecursos(request,id):
        RecursosPro.objects.filter(CodigoRecursos=id).delete()
        return redirect(to="listarRecursos")

    def editarRecursos(request,id):
        actua= RecursosPro.objects.get(CodigoRecursos=id)
        data = {
            'form': FormularioRecursosPro(instance=actua)
        }
        if request.method == 'POST':
            formulario = FormularioRecursosPro(data=request.POST, instance=actua)
            if formulario.is_valid():
                formulario.save()
                data['mensaje']= "Se Actualizo el Registro."
                data['form']=formulario

        return render(request, 'modificarRecursos.html', data)

    def ReportPDF(self, *args, **kwargs):

            template = get_template('ReportePDF4.html')
            context = {'report': RecursosPro.objects.all(),
                       'comp': {'name': 'Reporte de Recursos'}
                       }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition']= 'attachment; filename="report.pdf"'
            pisaStatus = pisa.CreatePDF(

            html, dest=response)

            if pisaStatus.err:
                return HttpResponse('we had some errors <pre>' + html + '</pre>')

            return response
