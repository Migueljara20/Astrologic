from django.urls import path
from .views import imagenes_nasa_view

urlpatterns = [
    path('', imagenes_nasa_view, name='imagenes_nasa'),
]