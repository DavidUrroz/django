from rest_framework.serializers import ModelSerializer
from .models import Videojuego

class VideojuegoSerializer(ModelSerializer):
    class Meta:
        model = Videojuego
        fields = "__all__"