from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirecionar para a página inicial após o login
        else:
            # Retornar uma mensagem de erro
            return render(request, 'login.html', {'error': 'Credenciais inválidas'})
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o usuário
            login(request, user)  # Faz o login do usuário após o registro
            return redirect('home')  # Redireciona para a página inicial ou outra página
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})
