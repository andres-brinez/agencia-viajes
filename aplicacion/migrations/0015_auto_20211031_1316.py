# Generated by Django 3.2.7 on 2021-10-31 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0014_delete_suscripcion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programar',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='programar',
            name='personas',
        ),
        migrations.AddField(
            model_name='programar',
            name='creacion',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='programar',
            name='modificacion',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
