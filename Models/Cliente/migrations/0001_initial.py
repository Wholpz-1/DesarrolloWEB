# Generated by Django 3.0.8 on 2020-08-22 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('CodigoCliente', models.AutoField(primary_key=True, serialize=False)),
                ('NombreCliente', models.CharField(max_length=75)),
                ('Direccion', models.CharField(max_length=75)),
                ('Telefono', models.CharField(max_length=12)),
            ],
        ),
    ]