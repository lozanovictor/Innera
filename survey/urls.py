from django.urls import path
from .views import questionario_view

urlpatterns = [
    path('questionario/', questionario_view, name='questionario'),
]