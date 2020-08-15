from django.http import HttpRequest
from django.shortcuts import render, redirect

from Models.Empleado.forms import FormularioEmpleado
from Models.Empleado.models import Empleado


class FormularioEmpleadoView(HttpRequest):
    def index(request):
        empleado = FormularioEmpleado()
        return render(request, "EmpleadoIndex.html", {"form":empleado})

    def procesar_formulario(request):
        empleado = FormularioEmpleado(request.POST)
        if empleado.is_valid():
            empleado.save()
            empleado = FormularioEmpleado()

            return render(request, "EmpleadoIndex.html", {"form":empleado, "mensaje": 'ok'})

    def listar_empleados(request):
        empleado = Empleado.objects.all()
        return render(request, "ListaEmpleado.html", {"empleados":empleado})

    def eliminarEmpleado(request,id):
        Empleado.objects.filter(CodigoEmpleado=id).delete()
        return redirect(to="listarEmpleado")

    def editarEmpleado(request, id):
        actua= Empleado.objects.get(CodigoEmpleado=id)
        data = {
            'form': FormularioEmpleado(instance=actua)
        }
        if request.method == 'POST':
            formulario = FormularioEmpleado(data=request.POST, instance=actua)
            if formulario.is_valid():
                formulario.save()
                data['mensaje']= "Se Actualizo el Registro."
                data['form']=formulario

        return render(request, 'modificarEmpleado.html',data)