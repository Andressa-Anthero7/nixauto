from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('display', views.display, name='display'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('anunciar', views.anunciar, name='anunciar'),
    path('imagens', views.imagens, name='imagens'),


]