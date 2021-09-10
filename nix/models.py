from django.db import models
from django_resized import ResizedImageField
from sorl.thumbnail import ImageField, get_thumbnail

# Create your models here.


class Anuncio(models.Model):
    

    titulo = models.CharField(max_length=20, null=False, blank=False)
    modelo = models.CharField(max_length=20, null=False, blank=False)
    marca = models.CharField(max_length=20, default=0, null=False, blank=False, )
    ano = models.CharField(max_length=4, default=1950, null=False, blank=False)
    valor = models.CharField(max_length=20, null=False, blank=False)
    contato = models.CharField(max_length=20, null=False, blank=False)
    anunciante = models.CharField(null=False, max_length=20, blank=False)
    imagem = ResizedImageField(size=[220, 180], quality=100 ,upload_to ='media/')
    

    def publish(self):
        self.save()

    def __str__(self):
        return self.titulo



