# Generated by Django 3.2.6 on 2021-09-14 18:13

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('nix', '0005_alter_anuncio_valor'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='km',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='imagem1',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='PNG', keep_meta=True, quality=100, size=[660, 540], upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='imagem10',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, size=[660, 540], upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='imagem2',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='PNG', keep_meta=True, quality=100, size=[660, 540], upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='imagem3',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='PNG', keep_meta=True, quality=100, size=[660, 540], upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='imagem4',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='PNG', keep_meta=True, quality=100, size=[660, 540], upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='imagem5',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='PNG', keep_meta=True, quality=100, size=[660, 540], upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='imagem6',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='PNG', keep_meta=True, quality=100, size=[660, 540], upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='imagem7',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, size=[660, 540], upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='imagem8',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, size=[660, 540], upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='imagem9',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='PNG', keep_meta=True, null=True, quality=100, size=[660, 540], upload_to='media/'),
        ),
    ]
