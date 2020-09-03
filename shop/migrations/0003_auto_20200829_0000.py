# Generated by Django 3.0.7 on 2020-08-29 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200828_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación'),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización'),
        ),
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Altura del Producto (en cm)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='Peso del Producto (en Kg)'),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Anchura del Producto (en cm)'),
        ),
    ]