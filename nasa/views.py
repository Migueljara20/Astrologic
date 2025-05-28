from django.shortcuts import render
import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta
from deep_translator import GoogleTranslator #libreria para traduccion



# Create your views here.
load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY")
NASA_API_URL = os.getenv("NASA_API_URL")

def imagenes_nasa_view(request):
    hoy = datetime.today().date()
    fechas = [hoy - timedelta(days=i) for i in range(5)]
    imagenes = []

    for fecha in fechas:
        fecha_str = fecha.strftime('%Y-%m-%d')
        url = f"{NASA_API_URL}?api_key={NASA_API_KEY}&date={fecha_str}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

                # Traducimos título y explicación
            data["title"] = GoogleTranslator(source='en', target='es').translate(data["title"])
            data["explanation"] = GoogleTranslator(source='en', target='es').translate(data["explanation"])

            imagenes.append(data)
        else:
            print(f"Error en fecha {fecha_str}: {response.status_code}")

    return render(request, 'pages/imagenes_nasa.html', {'imagenes': imagenes})
