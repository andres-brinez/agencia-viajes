# Generated by Django 3.2.7 on 2021-10-27 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0008_alter_programar_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programar',
            name='correo',
            field=models.EmailField(default=None, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='programar',
            name='edad',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='programar',
            name='nombre',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]