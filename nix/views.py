from django.shortcuts import render

from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from nix.forms import CriarAnuncioForms
from .models import Anuncio
from django.db.models import Q

import random 


# Create your views here.

def index(request):
    posts = Anuncio.objects.order_by('?')[:3]
    carousel = Anuncio.objects.order_by('?')[:3]
    carousel_mobile1 = Anuncio.objects.order_by('?')[:1]
    carousel_mobile2 = Anuncio.objects.order_by('?')[:1]
    carousel_mobile3 = Anuncio.objects.order_by('?')[:1]
    carousel_mobile4 = Anuncio.objects.order_by('?')[:1]
    carousel_mobile5 = Anuncio.objects.order_by('?')[:1]
    carousel_mobile6 = Anuncio.objects.order_by('?')[:1]

    busca = request.GET.get('search')
    if busca:
        posts = Anuncio.objects.filter(
            Q(titulo__icontains=busca)|Q(modelo__icontains=busca)|Q(marca__icontains=busca)|Q(ano__icontains=busca)|Q(valor__icontains=busca)|Q(anunciante__icontains=busca)
        )









    return render(request, 'nix/index.html',{'posts': posts, 'fotos':carousel, 'carousel_mobile1':carousel_mobile1, 'carousel_mobile2':carousel_mobile2, 'carousel_mobile3':carousel_mobile3, 'carousel_mobile4':carousel_mobile4, 'carousel_mobile5':carousel_mobile5, 'carousel_mobile6':carousel_mobile6}  )


def anunciar(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CriarAnuncioForms(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # redirect to a new URL:
            return HttpResponseRedirect('/display')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = CriarAnuncioForms()
    contexto = {'form': form}
    return render(request, 'nix/anunciar.html', contexto)


def cadastro(request):
    return render(request, 'nix/cadastro.html')

def display (request):
    posts = Anuncio.objects.all()
    return  render(request, 'nix/display.html',{'posts': posts})

def imagens (request):
    imagem = Anuncio.objects.all()
    return render(request,{'imagens': imagem})

