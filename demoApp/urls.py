from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register("videojuegos", views.VideojuegosViewset)

urlpatterns = [
]

urlpatterns += router.urls

# router .urls es el conjunto de todos los register