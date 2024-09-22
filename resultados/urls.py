from django.urls import path
from .views import resultados

urlspatterns = [
    path("resultados/", resultados, "resultados.html")
]
