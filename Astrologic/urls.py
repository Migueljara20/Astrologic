"""
URL configuration for Astrologic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from noticias.views import inicio_view, noticias_view
from nasa.views import imagenes_nasa_view
from galeria.views import galeria_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio_view, name="inicio"),
    path('noticias/', noticias_view, name="noticias"),
    path('nasa/', imagenes_nasa_view, name="imagenes_nasa"),
    path('galeria/', galeria_view, name="galeria"),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)