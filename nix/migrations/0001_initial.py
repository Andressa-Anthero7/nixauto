# Generated by Django 3.2.6 on 2021-08-04 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=20)),
                ('marca', models.CharField(default=0, max_length=20)),
                ('modelo', models.CharField(max_length=20)),
                ('ano', models.CharField(default=1950, max_length=4)),
                ('valor', models.CharField(max_length=20)),
                ('contato', models.CharField(max_length=20)),
                ('anunciante', models.CharField(max_length=20)),
                ('imagem', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
