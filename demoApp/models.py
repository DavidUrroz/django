from django.db import models

# Create your models here.

class Videojuego(models.Model):
    nombre = models.CharField(max_length=100)
    anio_lanzamiento = models.CharField(max_length=100, blank=True)