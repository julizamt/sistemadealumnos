# Generated by Django 3.1.2 on 2020-11-10 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0015_auto_20201110_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='calif_anual',
            field=models.CharField(blank=True, default=None, error_messages={'unique': 'Ya existe un estudiante con este calificador anual ↓'}, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='disposicion',
            field=models.CharField(blank=True, default=None, error_messages={'unique': 'Esta disposición ya fue asignada ↓'}, max_length=6, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='dni',
            field=models.CharField(error_messages={'required': 'Ingresar DNI ↓', 'unique': 'Ya existe un estudiante con este DNI ↓'}, max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='ingreso',
            field=models.CharField(error_messages={'required': 'Ingresar año de ingreso ↓'}, max_length=4),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='last',
            field=models.CharField(error_messages={'required': 'Ingresar apellido ↓'}, max_length=200),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='name',
            field=models.CharField(error_messages={'required': 'Ingresar nombre ↓'}, max_length=200),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='trayectoria',
            field=models.CharField(blank=True, default=None, error_messages={'unique': 'Ya existe un estudiante con este calificador personal ↓'}, max_length=200, null=True, unique=True),
        ),
    ]
