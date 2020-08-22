from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, request
from django.shortcuts import render, redirect
from django.template.loader import get_template
from xhtml2pdf import pisa

from Models.Proyecto.forms import FormularioProyect
from Models.Proyecto.models import Proyecto



class FormularioProyectoView(HttpRequest):

    def index(request):
        proyecto = FormularioProyect()
        return render(request, "ProyectosIndex.html", {"form": proyecto})

    def procesar_formulario(request):
        proyecto = FormularioProyect(request.POST)
        if proyecto.is_valid():
            proyecto.save()
            proyecto = FormularioProyect()

            return render(request, "ProyectosIndex.html", {"form":proyecto, "mensaje": 'ok'})

    def listar_proyectos(request):
        proyectos = Proyecto.objects.all()
        return render(request, "ListaProyectos.html", {"proyectos" : proyectos})

    def eliminarProyecto(request,id):
        Proyecto.objects.filter(CodigoProyecto=id).delete()
        return redirect(to="listarProyecto")

    def editarProyecto(request, id):
        actua= Proyecto.objects.get(CodigoProyecto=id)
        data = {
            'form': FormularioProyect(instance=actua)
        }
        if request.method == 'POST':
            formulario = FormularioProyect(data=request.POST, instance=actua)
            if formulario.is_valid():
                formulario.save()
                data['mensaje']= "Se Actualizo el Registro."
                data['form']=formulario

        return render(request, 'modificarProyectos.html', data)

    def Reportpdf(self, *args, **kwargs):

            template = get_template('Reportpdf.html')
            context = {'report': Proyecto.objects.all(),
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

