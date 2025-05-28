from django.shortcuts import render
from django.shortcuts import render
from deep_translator import GoogleTranslator
import requests
import random

# Create your views here.

palabras_clave = ["mars", "moon", "galaxy", "nebula", "apollo", "jupiter"]
palabra = random.choice(palabras_clave)

url = f"https://images-api.nasa.gov/search?q={palabra}&media_type=image"

def galeria_view(request):    
    response = requests.get(url)
    imagenes = []

    if response.status_code == 200:
        data = response.json()
        items = data["collection"]["items"][:12]  # Mostrar 12 resultados

        for item in items:
            datos = item["data"][0]
            links = item.get("links", [])

            imagen = links[0]["href"] if links else None
            titulo = GoogleTranslator(source='en', target='es').translate(datos.get("title", "Sin título"))
            descripcion = GoogleTranslator(source='en', target='es').translate(datos.get("description", "Sin descripción"))

            imagenes.append({
                "titulo": titulo,
                "descripcion": descripcion,
                "imagen": imagen
            })

    return render(request, 'pages/galeria.html', {"imagenes": imagenes})