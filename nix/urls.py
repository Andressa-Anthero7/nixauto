from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('anunciar', views.anunciar, name='anunciar'),
    path('imagens', views.imagens, name='imagens'),
    path('', include('anunciante.urls')),

    path('anunciante',views.anunciante, name='anunciante'),

]