# Generated by Django 3.2.7 on 2021-11-01 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nix', '0015_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='tipo',
            field=models.CharField(choices=[('CARRO', 'CARRO'), ('MOTO', 'MOTO')], help_text='selecione Tipo do Veículo', max_length=20),
        ),
    ]