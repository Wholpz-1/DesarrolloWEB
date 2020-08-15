
"""DesswebGrupo4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Models.Empleado.views import FormularioEmpleadoView
from Models.Proyectos.views import FormularioProyectoView
from views.HomeView import HomeView
urlpatterns = [
    #path('admin/',  admin.site.urls),
    path('',HomeView.home,name='home'),
    path('registrarEmpleado/', FormularioEmpleadoView.index, name='registrarEmpleado'),
    path('guardarEmpleado/', FormularioEmpleadoView.procesar_formulario, name='guardarEmpleado'),
    path('listaEmpleado/', FormularioEmpleadoView.listar_empleados, name='listarEmpleado'),
    path('eliminarEmpleado/<id>', FormularioEmpleadoView.eliminarEmpleado, name='eliminarEmpleado'),
    path('editarEmpleado/<id>', FormularioEmpleadoView.editarEmpleado, name='editarEmpleado'),

    path('registrarProyecto/', FormularioProyectoView.index, name='registrarProyecto'),
    path('guardarProyecto/', FormularioProyectoView.procesar_formulario, name='guardarProyecto'),
    path('listaProyecto/', FormularioProyectoView.listar_proyectos, name='listarProyecto'),
    path('eliminarProyecto/<id>', FormularioProyectoView.eliminarProyecto, name='eliminarProyecto'),
    path('editarProyecto/<id>', FormularioProyectoView.editarProyecto, name='editarProyecto'),





]
