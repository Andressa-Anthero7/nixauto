from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponseRedirect, render, redirect
from nix.forms import CriarAnuncioForm
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
            Q(modelo__icontains=busca)|Q(marca__icontains=busca)|Q(ano_fabricacao__icontains=busca)|Q(ano_modelo__icontains=busca)|Q(combustivel__icontains=busca)|Q(cambio__icontains=busca)|Q(cor__icontains=busca)|Q(portas__icontains=busca)|Q(valor__icontains=busca)|Q(anunciante__icontains=busca)
        )
    return render(request, 'nix/index.html',{'posts': posts, 'fotos':carousel, 'carousel_mobile1':carousel_mobile1, 'carousel_mobile2':carousel_mobile2, 'carousel_mobile3':carousel_mobile3, 'carousel_mobile4':carousel_mobile4, 'carousel_mobile5':carousel_mobile5, 'carousel_mobile6':carousel_mobile6}  )


def anunciar(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CriarAnuncioForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            anuncio = form.save( commit=False )
            anuncio.anunciante = request.user
            anuncio.save()
            # redirect to a new URL:
            return  redirect('anuncio', pk=anuncio.pk)

        # if a GET (or any other method) we'll create a blank form
    else:
        form = CriarAnuncioForm()
    return render(request, 'nix/anunciar.html', {'form': form})


def anuncio(request,pk):
    post = get_object_or_404(Anuncio, pk=pk)
    return render(request,'nix/anuncio.html',{'post':post})

def anuncio_editar(request,pk):
    post =  get_object_or_404(Anuncio, pk=pk)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CriarAnuncioForm(request.POST, request.FILES, instance= post)
        # check whether it's valid:
        if form.is_valid():
            anuncio = form.save( commit=False )
            anuncio.anunciante = request.user
            anuncio.save()
            # redirect to a new URL:
            return  redirect('anuncio', pk=anuncio.pk)

        # if a GET (or any other method) we'll create a blank form
    else:
        form = CriarAnuncioForm(instance=post)
    return render(request, 'nix/anuncio_editar.html', {'form': form}) 

def anuncio_deletar(request,pk):
    post =  get_object_or_404(Anuncio, pk=pk)
    post.delete()
    return redirect('anunciante')

     
def anunciante (request):
    posts = Anuncio.objects.all()
    return  render(request, 'nix/area-anunciante.html',{'posts': posts})




