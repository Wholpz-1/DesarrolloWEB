# Generated by Django 3.0.8 on 2020-08-20 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoProyecto',
            fields=[
                ('CodigoTipoPro', models.AutoField(primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=75)),
            ],
        ),
    ]
