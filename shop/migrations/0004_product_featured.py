# Generated by Django 3.0.7 on 2020-08-29 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200829_0000'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured',
            field=models.BooleanField(default=False, verbose_name='¿Producto Featured?'),
        ),
    ]
