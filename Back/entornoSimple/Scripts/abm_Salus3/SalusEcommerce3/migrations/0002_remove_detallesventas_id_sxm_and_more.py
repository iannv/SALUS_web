# Generated by Django 4.2.2 on 2023-06-17 03:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalusEcommerce3', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallesventas',
            name='id_SXM',
        ),
        migrations.RemoveField(
            model_name='detallesventas',
            name='id_V',
        ),
        migrations.RemoveField(
            model_name='historialesmedicos',
            name='id_MP',
        ),
        migrations.RemoveField(
            model_name='historialesmedicos',
            name='id_TE',
        ),
        migrations.RemoveField(
            model_name='medicospacientes',
            name='id_UM',
        ),
        migrations.RemoveField(
            model_name='medicospacientes',
            name='id_UP',
        ),
        migrations.RemoveField(
            model_name='serviciosxmedicos',
            name='id_S',
        ),
        migrations.RemoveField(
            model_name='serviciosxmedicos',
            name='id_UM',
        ),
        migrations.RemoveField(
            model_name='usuariosmedicos',
            name='id_C',
        ),
        migrations.RemoveField(
            model_name='usuariospacientes',
            name='id_C',
        ),
        migrations.RemoveField(
            model_name='ventas',
            name='id_C',
        ),
        migrations.AlterField(
            model_name='ventas',
            name='FechaVenta_V',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.DeleteModel(
            name='Cuentas',
        ),
        migrations.DeleteModel(
            name='DetallesVentas',
        ),
        migrations.DeleteModel(
            name='HistorialesMedicos',
        ),
        migrations.DeleteModel(
            name='MedicosPacientes',
        ),
        migrations.DeleteModel(
            name='ServiciosXMedicos',
        ),
        migrations.DeleteModel(
            name='TiposEstudios',
        ),
    ]
