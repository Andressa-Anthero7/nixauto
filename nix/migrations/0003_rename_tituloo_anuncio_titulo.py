# Generated by Django 3.2.6 on 2021-08-04 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nix', '0002_rename_titulo_anuncio_tituloo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anuncio',
            old_name='tituloo',
            new_name='titulo',
        ),
    ]
