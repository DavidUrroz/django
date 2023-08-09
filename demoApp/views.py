from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import VideojuegoSerializer
from .models import Videojuego
# Create your views here.

class VideojuegosViewset(ModelViewSet):
    queryset = Videojuego.objects.all()
    serializer_class = VideojuegoSerializer