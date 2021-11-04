from django import forms
from nix.models import Anuncio, Proposta, Cadastro


class CriarAnuncioForm(forms.ModelForm):
    class Meta:
        model = Anuncio
        fields = (
            'tipo',
            'marca',
            'modelo',
            'ano_fabricacao',
            'ano_modelo',
            'combustível',
            'cambio',
            'cor',
            'portas',
            'valor',
            'contato',
            'acessórios_opcionais',
            'imagem1',
            'imagem2',
            'imagem3',
            'imagem4',
            'imagem5',
            'imagem6',
            'imagem7',
            'imagem8',
            'imagem9',
            'imagem10',
        )
        widgets = {'tipo': forms.Select(attrs={'onchange': "exibir_ocultar();"})}
         



class PropostaForm(forms.ModelForm):
    class Meta:
        model = Proposta
        fields = '__all__'


class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = '__all__'
