# Generated by Django 3.1.2 on 2020-11-07 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0010_auto_20201107_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='calif_anual',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='trayectoria',
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
    ]
