from django.db import models

# Create your models here.


class Anuncio (models.Model):
    STATUS = (
        ('active','Ativo'),
        ('draft','Rascunho')
    )

    titulo = models.CharField(max_length=20, null=False,blank=False)
    marca = models.CharField(max_length=20, default=0, null=False, blank=False, )
    modelo = models.CharField(max_length=20, null=False, blank=False)
    ano = models.CharField(max_length=4,default=1950,null=False,blank=False)
    valor =  models.CharField(max_length=20,null=False,blank=False)
    contato = models.CharField(max_length=20,null=False,blank=False)
    anunciante = models.CharField(null=False,max_length=20,blank=False)
    imagem = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.titulo







