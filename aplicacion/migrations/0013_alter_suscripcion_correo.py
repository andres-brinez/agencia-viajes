# Generated by Django 3.2.7 on 2021-10-30 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0012_planear'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suscripcion',
            name='correo',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]
