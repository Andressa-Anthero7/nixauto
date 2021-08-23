from django.shortcuts import render

from django.shortcuts import HttpResponseRedirect
from django.shortcuts import render
from nix.forms import CriarAnuncioForms
from .models import Anuncio

import random 


# Create your views here.

def index(request):
    posts = Anuncio.objects.all()
    posts = random.sample(posts.items(), 9)
    return render(request, 'nix/index.html',{'posts': posts})


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

