# Generated by Django 3.0.8 on 2020-08-22 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Cliente', '0001_initial'),
        ('TipoProyecto', '0001_initial'),
        ('Empleado', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='proyect',
            fields=[
                ('CodigoProyecto', models.AutoField(primary_key=True, serialize=False)),
                ('NombreProyecto', models.CharField(max_length=75)),
                ('FechaInicio', models.DateField()),
                ('FechaEntrega', models.DateField()),
                ('cliente_CodigoCliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cliente.Cliente')),
                ('empleado_CodigoEmpleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empleado.Empleado')),
                ('tipopro_CodigoTipoPro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TipoProyecto.TipoProyecto')),
            ],
        ),
    ]
