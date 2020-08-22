from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render, redirect
from django.template.loader import get_template
from xhtml2pdf import pisa

from Models.proyect.forms import FormularioProyecto
from Models.proyect.models import proyect



class FormularioProyectoView(HttpRequest):

    def index(request):
        proyecto = FormularioProyecto()
        return render(request, "ProyectosIndex.html", {"form": proyecto})

    def procesar_formulario(request):
        proyecto = FormularioProyecto(request.POST)
        if proyecto.is_valid():
            proyecto.save()
            proyecto = FormularioProyecto()

            return render(request, "ProyectosIndex.html", {"form":proyecto, "mensaje": 'ok'})

    def listar_proyectos(request):
        proyectos = proyect.objects.all()
        return render(request, "ListaProyectos.html", {"proyectos" : proyectos})

    def eliminarProyecto(request,id):
        proyect.objects.filter(CodigoProyecto=id).delete()
        return redirect(to="listarProyecto")

    def editarProyecto(request, id):
        actua= proyect.objects.get(CodigoProyecto=id)
        data = {
            'form': FormularioProyecto(instance=actua)
        }
        if request.method == 'POST':
            formulario = FormularioProyecto(data=request.POST, instance=actua)
            if formulario.is_valid():
                formulario.save()
                data['mensaje']= "Se Actualizo el Registro."
                data['form']=formulario

        return render(request, 'modificarProyectos.html', data)

    def Reportpdf(self, *args, **kwargs):

            template = get_template('Reportpdf.html')
            context = {'report': proyect.objects.all(),
                       'comp': {'name': 'Reporte de Proyectos'}
                       }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition']= 'attachment; filename="report.pdf"'
            pisaStatus = pisa.CreatePDF(

            html, dest=response)

            if pisaStatus.err:
                return HttpResponse('we had some errors <pre>' + html + '</pre>')

            return response
