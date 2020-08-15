from django.http import HttpRequest
from django.shortcuts import render, redirect

from Models.Proyectos.forms import FormularioProyecto
from Models.Proyectos.models import Proyecto


class FormularioProyectoView(HttpRequest):
    def index(request):
        proyecto = FormularioProyecto()
        return render(request, "ProyectoIndex.html", {"form":proyecto})

    def procesar_formulario(request):
        proyecto = FormularioProyecto(request.POST)
        if proyecto.is_valid():
            proyecto.save()
            proyecto = FormularioProyecto()

            return render(request, "ProyectoIndex.html", {"form":proyecto, "mensaje": 'ok'})

    def listar_proyectos(request):
        proyectos = Proyecto.objects.all()
        return render(request, "ListaProyecto.html", {"proyectos" : proyectos})

    def eliminarProyecto(request,id):
        Proyecto.objects.filter(CodigoProyecto=id).delete()
        return redirect(to="listarProyecto")

    def editarProyecto(request, id):
        actua= Proyecto.objects.get(CodigoProyecto=id)
        data = {
            'form': FormularioProyecto(instance=actua)
        }
        if request.method == 'POST':
            formulario = FormularioProyecto(data=request.POST, instance=actua)
            if formulario.is_valid():
                formulario.save()
                data['mensaje']= "Se Actualizo el Registro."
                data['form']=formulario

        return render(request, 'modificarProyecto.html', data)
