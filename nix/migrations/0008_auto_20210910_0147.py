# Generated by Django 3.2.6 on 2021-09-10 04:47

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('nix', '0007_anuncio_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnuncioPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='anuncio',
            name='imagem',
        ),
    ]
