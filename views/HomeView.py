from django.http import HttpResponse
from django.template.loader import get_template


class HomeView():
    def home(self):
        plantilla= get_template('index.html')
        return HttpResponse(plantilla.render())
    def pagina1(self):
        return HttpResponse('hola desde una nueva ruta')
    def pagina2(self,parametro1):
        return HttpResponse('hola desde otra ruta con parametro' + str(parametro1))
    def pagina3(self,parametro1,parametro2):
        return HttpResponse('hola desde otra ruta con 2 parametro' + str(parametro1) + ' - ' + str(parametro2))
    def formulario(self):
        plantilla = get_template('formulario.html')
        return HttpResponse(plantilla.render())