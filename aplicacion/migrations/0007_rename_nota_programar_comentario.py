# Generated by Django 3.2.7 on 2021-10-24 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0006_rename_n_personas_programar_personas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programar',
            old_name='nota',
            new_name='comentario',
        ),
    ]
