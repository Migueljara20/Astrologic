from django.shortcuts import render
import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Conectar con MongoDB
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
noticias_collection = db[MONGO_COLLECTION]

# Vista para mostrar noticias
def noticias_view(request):
    query = request.GET.get("q")  # Soporte para búsqueda opcional

    if query:
        noticias = list(noticias_collection.find({
            "nombre": {"$regex": query, "$options": "i"}
        }))
    else:
        noticias = list(noticias_collection.find())

    return render(request, 'pages/noticias.html', {"noticias": noticias})

# Vista de inicio
def inicio_view(request):
    return render(request, 'pages/inicio.html')

