from django import forms
from .models import Questionario
from datetime import datetime, timedelta

class Questionarios(forms.ModelForm):
    
    CHOICES = [
        ('0', 'Nenhuma no último mês'),
        ('1', 'Menos de uma vez por semana'),
        ('2', 'Uma ou duas vezes por semana'),
        ('3', 'Três ou mais vezes por semana'),
    ]

    CHOICES2 = [
        ('0', 'Muito boa'),
        ('1', 'Boa'),
        ('2', 'Ruim'),
        ('3', 'Muito Ruim'),
    ]

    CHOICES3 = [
        ('0', 'Nenhuma dificuldade'),
        ('1', 'Um problema leve'),
        ('2', 'Um problema razoavel'),
        ('3', 'Um grande problema'),
    ]

    CHOICES4 = [
        ('0', 'Não'),
        ('1', 'Parceiro ou colega, mas em outro quarto'),
        ('2', 'Parceiro no mesmo quarto, mas em outra cama'),
        ('3', 'Parceiro na mesma cama'),
    ]
    
    questao1 = forms.TimeField( 
          label= "1- Durante o último mês, quando você geralmente foi para a cama a noite?",
          help_text="No formato HH:MM",
          widget=forms.TimeInput(format='%H:%M') )
    
    questao2 = forms.IntegerField( 
          label= "2- Durante o último mês, quanto tempo (em minutos) você geralmente levou para dormir a noite?",
          help_text="Digite o número inteiro de minutos" )
    
    questao3 = forms.TimeField( 
          label = "3- Durante o último mês, quando você geralmente levantou de manhã?",
          help_text="No formato HH:MM",
          widget=forms.TimeInput(format='%H:%M') )
    
    questao4 = forms.IntegerField( 
          label = "4- Durante o último mês, quantas horas de sono você teve por noite? (Este pode ser diferente do número de horas que você ficou na cama)",
          help_text="Digite o número inteiro de horas")
    
    questao5 = forms.CharField(
        label="5- Durante o último mês, com que frequência você teve dificuldade para dormir porque você...",
        disabled=True, 
        required=False,
    )

    questao5a = forms.ChoiceField(
        label = "A) não conseguiu adormecer em até 30 minutos",
        widget=forms.RadioSelect,
        choices=CHOICES,
    )
    questao5b = forms.ChoiceField(
        label="B) acordou no meio da noite ou de manhã cedo",
        widget=forms.RadioSelect,
        choices=CHOICES,
    )
    questao5c = forms.ChoiceField(
        label="C) precisou levantar para ir ao banheiro",
        widget=forms.RadioSelect,
        choices=CHOICES,
    )
    questao5d = forms.ChoiceField(
        label="D) não conseguiu respirar confortavelmente",
        widget=forms.RadioSelect,
        choices=CHOICES,
    )
    questao5e = forms.ChoiceField(
        label="E) tossiu ou roncou forte",  
        widget=forms.RadioSelect,
        choices=CHOICES,
    )
    questao5f = forms.ChoiceField(
        label = "F) sentiu muito frio",
        widget=forms.RadioSelect,
        choices=CHOICES,
    )
    questao5g = forms.ChoiceField(
        label="G) sentiu muito calor",
        widget=forms.RadioSelect,
        choices=CHOICES,
    )
    questao5h = forms.ChoiceField(
        label="H) teve sonhos ruins",
        widget=forms.RadioSelect,
        choices=CHOICES,
    )
    questao5i = forms.ChoiceField(
        label="I) teve dor",
        widget=forms.RadioSelect,
        choices=CHOICES,
    )
    questao5j1 = forms.CharField(
        label ="J) outra(s) razão(ões), por favor descreva:",
        max_length=300,
        required=False,
    )
    questao5j2 = forms.ChoiceField(
        label="Com que frequência, durante o último mês, você teve dificuldade para dormir devido a essa razão?",
        widget=forms.RadioSelect,
        choices=CHOICES,
    )
    questao6 = forms.ChoiceField(
        label="6. Durante o último mês como você classificaria a qualidade do seu sono de uma maneira geral:",
        widget=forms.RadioSelect,
        choices=CHOICES2,
    )
    questao7 = forms.ChoiceField(
        label="7. Durante o último mês, com que frequência você tomou medicamento (prescrito ou “por conta própria”) para lhe ajudar a dormir?",
        widget=forms.RadioSelect,
        choices=CHOICES,
    )
    questao8 = forms.ChoiceField(
        label="8. No último mês, que frequência você teve dificuldade para ficar acordado enquanto dirigia, comia ou participava de uma atividade social (festa, reunião de amigos, trabalho, estudo)",
        widget=forms.RadioSelect,
        choices=CHOICES,
    )
    questao9 = forms.ChoiceField(
        label="9. Durante o último mês, quão problemático foi pra você manter o entusiasmo (ânimo) para fazer as coisas (suas atividades habituais)?",
        widget=forms.RadioSelect,
        choices=CHOICES3,
    )
    questao10 = forms.ChoiceField(
        label="10. Você tem um(a) parceiro [esposo (a)] ou colega de quarto?",
        widget=forms.RadioSelect,
        choices=CHOICES4,
    )

    class Meta:
        model = Questionario  # Relaciona ao modelo Questionario
        fields = ['questao1', 'questao2', 'questao3', 'questao4', 'questao5',
                  'questao5a', 'questao5b', 'questao5c', 'questao5d', 
                  'questao5e', 'questao5f', 'questao5g', 'questao5h', 
                  'questao5i', 'questao5j1', 'questao5j2', 'questao6', 'questao7', 
                  'questao8', 'questao9', 'questao10'] 
    
    def save(self, commit=True):
        # Chama o método save original
        instance = super().save(commit=False)

        #Processamento dos valores das questões
        #Valor da questão 2
        valorq2 = int(self.cleaned_data['questao2'])
        if valorq2 <= 15:
            questao2 = 0
        elif 16 <= valorq2 <= 30:
            questao2 = 1
        elif 31 <= valorq2 <= 60:
            questao2 = 2
        else:
            questao2 = 3

        #Valor do bloco 2
        bloco2 = questao2 + int(self.cleaned_data['questao5a'])
        if bloco2 == 0:
            bloco2 = 0
        elif bloco2 == 1 or bloco2 == 2:
            bloco2 = 1
        elif bloco2 == 3 or bloco2 == 4:
            bloco2 = 2
        else:
            bloco2 = 3

        #Valor da questão 4 - bloco 3
        questao4 = int(self.cleaned_data['questao4'])
        if questao4 > 7:
            questao4 = 0
        elif questao4 <= 7 and questao4 > 6:
            questao4 = 1
        elif questao4 <= 6 and questao4 > 5:
            questao4 = 2
        else:
            questao4 = 3

        #Valor da questão 2 - bloco 4
        quest4 = int(self.cleaned_data['questao4'])
        dormir = self.cleaned_data['questao1']
        acordar = self.cleaned_data['questao3']
        hoje = datetime.today()
        dormir_dt = datetime.combine(hoje, dormir)
        acordar_dt = datetime.combine(hoje, acordar)

        if acordar_dt < dormir_dt:
            acordar_dt += timedelta(days=1)

        dif = acordar_dt - dormir_dt
        horas = dif.total_seconds()/3600

        #Eficiencia do sono
        eficiencia = (quest4/horas)*100
        
        bloco4 = 0 #Armazena os pontos do bloco
        if eficiencia > 85:
            bloco4 = 0
        elif eficiencia >= 75 and eficiencia < 84:
            bloco4 = 1
        elif eficiencia >= 65 and eficiencia < 74:
            bloco4 = 2
        else:
            bloco4 = 3

        #Bloco 5
        soma5 = int(self.cleaned_data['questao5b']) + int(self.cleaned_data['questao5c']) + int(self.cleaned_data['questao5d']) + int(self.cleaned_data['questao5e']) + int(self.cleaned_data['questao5f']) + int(self.cleaned_data['questao5g']) + int(self.cleaned_data['questao5h']) + int(self.cleaned_data['questao5i']) + int(self.cleaned_data['questao5j2'])

        if soma5 == 0:
            bloco5 = 0
        elif soma5 >=1 and soma5 <=9:
            bloco5 = 1
        elif soma5 >=10 and soma5 <=18:
            bloco5 = 2
        else:
            bloco5 = 3

        #Bloco 7
        soma7 = int(self.cleaned_data['questao8']) + int(self.cleaned_data['questao9'])
        if soma7 == 0:
            bloco7 = 0
        elif soma7 >=1 and soma7 <= 2:
            bloco7 = 1
        elif soma7 >=3 and soma7 <= 4:
            bloco7 = 2
        else:
            bloco7 = 3

        resposta_total = 0
        resposta_total += int(self.cleaned_data['questao6']) + bloco2 + questao4 + bloco4 + bloco5 + int(self.cleaned_data['questao7']) + bloco7
        
        instance.resultado = resposta_total

        if commit:
            instance.save()
        return instance