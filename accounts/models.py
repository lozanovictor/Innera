from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)  # Campo de ID como chave primária (gerado automaticamente)
    
    def __str__(self):
        return self.username
