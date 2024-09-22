from django.db import models
from accounts.models import CustomUser  # Importa o modelo de usuário do Django

class Questionario(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Relaciona o questionário com o usuário
    questao1 = models.TimeField()  
    questao2 = models.IntegerField()
    questao3 = models.TimeField()  
    questao4 = models.IntegerField()
    questao5a = models.IntegerField()
    questao5b = models.IntegerField()
    questao5c = models.IntegerField()
    questao5d = models.IntegerField()
    questao5e = models.IntegerField()
    questao5f = models.IntegerField()
    questao5g = models.IntegerField()
    questao5h = models.IntegerField()
    questao5i = models.IntegerField()
    questao5j1 = models.CharField(max_length=300) 
    questao5j2 = models.IntegerField()
    questao6 = models.IntegerField()
    questao7 = models.IntegerField()
    questao8 = models.IntegerField()
    questao9 = models.IntegerField()
    questao10 = models.IntegerField()
    id = models.AutoField(primary_key=True)
    resultado = models.IntegerField() #Guarda a pontuação do questionario
    data_hora = models.DateTimeField(auto_now_add= True)
    

    def __str__(self):
        return f"Questionário #{self.id} - Usuário: {self.usuario.username}"