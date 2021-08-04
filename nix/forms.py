from django import forms


class CriarAnuncioForms(forms.Form):
    titulo = forms.CharField(label="Titulo", max_length=30)
    marca = forms.CharField(label="Marca", max_length=30)
    modelo = forms.CharField(label="Modelo", max_length=30)
    ano = forms.CharField(label="Ano", max_length=30)
    valor = forms.CharField(label="Valor", max_length=30)
    contato = forms.CharField(label="Contato", max_length=30)
    anunciante = forms.CharField(label="Anunciante", max_length=30)
