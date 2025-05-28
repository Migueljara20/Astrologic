from django.urls import path
from .views import noticias_view

urlpatterns = [
    path('', noticias_view, name='noticias'),
]
