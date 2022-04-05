from django.shortcuts import render, redirect, HttpResponse
from core.models import Evento
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def login_user(request):
    return render(request, 'agenda/login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

def submit_login(request):
    if(request.POST):
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if(usuario is not None):
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário e senha inválidos!")
    return redirect('/')    

@login_required(login_url='/login/')

def lista_eventos(request):
    usuario = request.user
    # usuario = request.user
    # evento = Evento.objects.get(id=1)
    # evento = Evento.objects.all()
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda/agenda.html', dados)