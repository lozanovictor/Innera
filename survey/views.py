from django.shortcuts import render, redirect
from .forms import Questionarios
from django.contrib.auth.decorators import login_required
from .models import Questionario

@login_required()
def questionario_view(request):
    if request.method == 'POST':
        form = Questionarios(request.POST)
        if form.is_valid():
            questionario = form.save(commit=False)  
            questionario.usuario = request.user  
            questionario.save()  
            return redirect('home')
    else:
        form = Questionarios()

    context = {'form': form}
    return render(request, 'questionario.html', context)