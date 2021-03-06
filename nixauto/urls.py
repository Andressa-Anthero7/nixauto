"""nixauto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nix.urls')),
    path('anunciar/',include('nix.urls')),
    path('anuncio/<int:pk>/',include('nix.urls')),
    path('anuncio/<int:pk>/editar/',include('nix.urls')),
    path('anuncio/<int:pk>/deletar/',include('nix.urls')),
    path('anunciante',include('nix.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('anunciante', include('anunciante.urls')),
    path('proposta',include('nix.urls')),
    path('cadastro', include('nix.urls')),

]

if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)