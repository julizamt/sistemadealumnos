# Generated by Django 3.1.2 on 2020-11-11 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretaria', '0019_auto_20201111_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='tipo',
            field=models.CharField(choices=[('Regular', 'Regular'), ('Egresado/a', 'Egresado/a'), ('Salido con pase', 'Salido/a con pase'), ('Salido sin pase', 'Salido/a sin pase')], default='Regular', max_length=64),
        ),
    ]
