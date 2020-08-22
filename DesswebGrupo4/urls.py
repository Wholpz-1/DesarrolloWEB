
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
from django.contrib.auth.views import LoginView, logout_then_login

from Models.Cliente.views import FormularioClienteView
from Models.Empleado.views import FormularioEmpleadoView
from Models.Proyecto.views import FormularioProyectoView
from Models.TipoProyecto.views import FormularioTipoProView
from views.HomeView import HomeView

urlpatterns = [
    path('admin/',  admin.site.urls),

    path('', LoginView.as_view(template_name='Login.html'), name="login"),
    path('logout/',logout_then_login, name ="logout"),
    path('inicio/', HomeView.home, name='home'),
path('', LoginView.as_view(template_name='Login.html'), name="login"),
    path('accounts/login/', LoginView.as_view(template_name='Login.html'), name="login"),


    path('registrarEmpleado/', FormularioEmpleadoView.index, name='registrarEmpleado'),
    path('guardarEmpleado/', FormularioEmpleadoView.procesar_formulario, name='guardarEmpleado'),
    path('listaEmpleado/', FormularioEmpleadoView.listar_empleados, name='listarEmpleado'),
    path('eliminarEmpleado/<id>', FormularioEmpleadoView.eliminarEmpleado, name='eliminarEmpleado'),
    path('editarEmpleado/<id>', FormularioEmpleadoView.editarEmpleado, name='editarEmpleado'),
    path('reporte_excel_proyecto/', FormularioEmpleadoView.Reportpdf, name='reporte_excel_proyecto'),

    path('registrarProyect/', FormularioProyectoView.index, name='registrarProyect'),
    path('guardarProyecto/', FormularioProyectoView.procesar_formulario, name='guardarProyecto'),
    path('listaProyecto/', FormularioProyectoView.listar_proyectos, name='listarProyecto'),
    path('eliminarProyecto/<id>', FormularioProyectoView.eliminarProyecto, name='eliminarProyecto'),
    path('editarProyecto/<id>', FormularioProyectoView.editarProyecto, name='editarProyecto'),
    path('ReportPdf/', FormularioProyectoView.Reportpdf, name='reportPDF'),


    path('registrarTipoPro/', FormularioTipoProView.index, name='registrarTipoPro'),
    path('guardarTipoPro/', FormularioTipoProView.procesar_formulario, name='guardarTipoPro'),
    path('listaTipoPro/', FormularioTipoProView.listar_TipoPro, name='listarTipoPro'),
    path('eliminarTipoPro/<id>', FormularioTipoProView.eliminarTiposPro, name='eliminarTipoPro'),
    path('editarTipoPro/<id>', FormularioTipoProView.editarTiposPro, name='editarTipoPro'),

    path('registrarCliente/', FormularioClienteView.index, name='registrarCliente'),
    path('guardarCliente/', FormularioClienteView.procesar_formulario, name='guardarCliente'),
    path('listaCliente/', FormularioClienteView.listar_Cliente, name='listarCliente'),
    path('eliminarCliente/<id>', FormularioClienteView.eliminarCliente, name='eliminarCliente'),
    path('editarCliente/<id>', FormularioClienteView.editarCliente, name='editarCliente'),
    path('ReportPDF/', FormularioClienteView.ReportPDF, name='ReportPDF'),

]
