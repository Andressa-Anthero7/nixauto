from django import forms
from nix.models import Anuncio



class CriarAnuncioForm(forms.ModelForm):
    class Meta:
    	model = Anuncio
    	fields = ('titulo','modelo', 'marca','ano', 'valor', 'contato','anunciante','imagem')

    

    