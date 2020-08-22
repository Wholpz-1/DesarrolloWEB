from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect


from Models.TipoProyecto.forms import FormularioTipoPro
from Models.TipoProyecto.models import TipoProyecto


class FormularioTipoProView(HttpRequest):
    def index(request):
        TipoPro = FormularioTipoPro()
        return render(request, "TipoProIndex.html", {"form":TipoPro})

    def procesar_formulario(request):
        TipoPro = FormularioTipoPro(request.POST)
        if TipoPro.is_valid():
            TipoPro.save()
            TipoPro = FormularioTipoPro()

            return render(request, "TipoProIndex.html", {"form":TipoPro, "mensaje": 'ok'})

    def listar_TipoPro(request):
        TipoPro = TipoProyecto.objects.all()
        return render(request, "ListaTiposPro.html", {"Tipos":TipoPro})

    def eliminarTiposPro(request,id):
        TipoProyecto.objects.filter(CodigoTipoPro=id).delete()
        return redirect(to="listarTipoPro")

    def editarTiposPro(request, id):
        actua= TipoProyecto.objects.get(CodigoTipoPro=id)
        data = {
            'form': FormularioTipoPro(instance=actua)
        }
        if request.method == 'POST':
            formulario = FormularioTipoPro(data=request.POST, instance=actua)
            if formulario.is_valid():
                formulario.save()
                data['mensaje']= "Se Actualizo el Registro."
                data['form']=formulario

        return render(request, 'modificarTipoPro.html',data)