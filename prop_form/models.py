from django.db import models
from django.conf import settings

# Create your models here.

class FormProp(models.Model):
	remetente = models.CharField(null=False, blank=False)
	mensagem = models.CharField( null=False, blank=False)


