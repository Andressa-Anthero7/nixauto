from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('anunciar/', views.anunciar, name='anunciar'),
  	path('anuncio/<int:pk>/', views.anuncio, name='anuncio'),
  	path('anuncio/<int:pk>/editar/', views.anuncio_editar, name='anuncio_editar'),
  	path('anuncio/<int:pk>/deletar/', views.anuncio_deletar, name='anuncio_deletar'),
    path('', include('anunciante.urls')),
    path('anunciante',views.anunciante, name='anunciante'),
    path('proposta', views.proposta, name='proposta'),
    path('cadastro',views.cadastro, name='cadastro'),
]