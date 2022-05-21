# Generated by Django 3.2.11 on 2022-05-19 05:55

import Modulos.Productos.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0014_alter_categoria_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='genero',
            name='abreviatura',
            field=Modulos.Productos.models.UpperField(blank=True, help_text='Ingrese la abreviatura a utilizar', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='abreviatura',
            field=Modulos.Productos.models.UpperField(blank=True, help_text='Ingrese la abreviatura a utilizar', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=Modulos.Productos.models.UpperField(max_length=150, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nit',
            field=Modulos.Productos.models.UpperField(max_length=10, verbose_name='Nit'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=Modulos.Productos.models.UpperField(max_length=150, verbose_name='Nombres'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=Modulos.Productos.models.UpperField(max_length=10, verbose_name='Nit'),
        ),
        migrations.AlterField(
            model_name='componente',
            name='abreviatura',
            field=Modulos.Productos.models.UpperField(blank=True, help_text='Ingrese la abreviatura a utilizar', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='componente',
            name='descripcion',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese la descripción descripción del ingrediente activo', max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='fabricante',
            name='abreviatura',
            field=Modulos.Productos.models.UpperField(blank=True, help_text='Ingrese la abreviatura a utilizar', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='fabricante',
            name='nombre',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese el nombre del fabricante', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='forma_pago',
            name='abreviatura',
            field=Modulos.Productos.models.UpperField(blank=True, help_text='Ingrese la abreviatura a utilizar', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='forma_pago',
            name='descripcion',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese la descripción de la forma de pago', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='genero',
            name='descripcion',
            field=Modulos.Productos.models.UpperField(max_length=50, unique=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='impuesto',
            name='abreviatura',
            field=Modulos.Productos.models.UpperField(default='', help_text='Ingrese la abreviatura a utilizar', max_length=10),
        ),
        migrations.AlterField(
            model_name='impuesto',
            name='descripcion',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese la descripción del impuesto', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='indicacion',
            name='descripcion',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese la descripción de la indicación', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='ubicacion',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese la ubicación del producto en la sucursal', max_length=100),
        ),
        migrations.AlterField(
            model_name='pais',
            name='abreviatura',
            field=Modulos.Productos.models.UpperField(blank=True, help_text='Ingrese la abreviatura a utilizar', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='pais',
            name='nombre',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese el nombre del país', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='presentacion',
            name='abreviatura',
            field=Modulos.Productos.models.UpperField(blank=True, help_text='Ingrese la abreviatura a utilizar', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='presentacion',
            name='descripcion',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese la descripción de la presentación (tabletas, jarabe, etc.)', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre_compra',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese el nombre para efectos de compras', max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre_corto',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese el nombre corto para facturación', max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre_venta',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese el nombre para efectos de ventas', max_length=60, unique=True),
        ),
        migrations.AlterField(
            model_name='producto_componente',
            name='cantidad',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese la cantidad de ingrediente activo en el producto', max_length=20),
        ),
        migrations.AlterField(
            model_name='producto_indicacion',
            name='dosis',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese la dosis del producto', max_length=20),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='contacto',
            field=Modulos.Productos.models.UpperField(max_length=150, verbose_name='Contacto'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='correo',
            field=Modulos.Productos.models.UpperField(max_length=150, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='direccion',
            field=Modulos.Productos.models.UpperField(max_length=150, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nit',
            field=Modulos.Productos.models.UpperField(max_length=150, verbose_name='Nit'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='nombre',
            field=Modulos.Productos.models.UpperField(max_length=150, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='telefono',
            field=Modulos.Productos.models.UpperField(max_length=150, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='abreviatura',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese la abreviatura a utilizar', max_length=8),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='descripcion',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese la descripción de la sucursal', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='direccion',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese la dirección de la sucursal', max_length=100),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='encargado',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese el nombre del encargado de la sucursal', max_length=100),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='telefono',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese el teléfono de la sucursal', max_length=30),
        ),
        migrations.AlterField(
            model_name='tipo_cliente',
            name='abreviatura',
            field=Modulos.Productos.models.UpperField(blank=True, help_text='Ingrese la abreviatura a utilizar', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='tipo_cliente',
            name='descripcion',
            field=Modulos.Productos.models.UpperField(max_length=25, unique=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='tipo_prescripcion',
            name='abreviatura',
            field=Modulos.Productos.models.UpperField(blank=True, help_text='Ingrese la abreviatura a utilizar', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='tipo_prescripcion',
            name='descripcion',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese la descripción del tipo de prescripción', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='unidad_medida',
            name='abreviatura',
            field=Modulos.Productos.models.UpperField(blank=True, help_text='Ingrese la abreviatura a utilizar', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='unidad_medida',
            name='descripcion',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese la descripción de la unidad de medida (caja, frasco, botella, etc.)', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='via_administracion',
            name='abreviatura',
            field=Modulos.Productos.models.UpperField(blank=True, help_text='Ingrese la abreviatura a utilizar', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='via_administracion',
            name='descripcion',
            field=Modulos.Productos.models.UpperField(help_text='Ingrese la descripción de la vía de administración (oral, tópica, vaginal, etc.)', max_length=100, unique=True),
        ),
    ]
