# Generated by Django 3.2.6 on 2021-08-30 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nix', '0003_rename_tituloo_anuncio_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='imagem',
            field=models.ImageField(height_field='200', upload_to='media/', width_field='150'),
        ),
    ]
