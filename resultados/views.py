from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from survey.models import Questionario
import matplotlib.pyplot as plt
import json
from io import BytesIO
import base64

@login_required
def resultados_usuario(request):
    questionarios = Questionario.objects.filter(usuario=request.user).values('data_hora', 'resultado').order_by('data_hora')
    
    datas = [q['data_hora'].strftime('%Y-%m-%d %H:%M:%S') for q in questionarios]
    resultados = [q['resultado'] for q in questionarios]
    
    # Criar o gráfico
    plt.figure(figsize=(10, 5))
    plt.plot(datas, resultados, marker='o')  # Plota os dados
    plt.title('Resultados do Questionário')
    plt.xlabel('Data')
    plt.ylabel('Resultado')
    plt.xticks(rotation=45)  # Rotaciona as labels do eixo X
    plt.tight_layout()
    
    # Salvar o gráfico em um buffer de bytes
    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    # Codifica a imagem em base64
    img_str = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    return render(request, 'home.html', {'img_str': img_str})

@login_required
def resultados_usuario(request):
    # Filtra os questionários preenchidos pelo usuário logado
    questionarios = Questionario.objects.filter(usuario=request.user).values('data_hora', 'resultado').order_by('data_hora')
    return render(request, 'home.html', {'questionarios': questionarios})