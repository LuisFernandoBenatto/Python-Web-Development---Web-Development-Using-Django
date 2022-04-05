from django.shortcuts import render, redirect, HttpResponse
from core.models import Evento
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime, timedelta

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
    data_atual = datetime.now() - timedelta(hours=1)
    evento = Evento.objects.filter(usuario=usuario,
                                   data_evento__gt=data_atual
                                  )
    dados = {'eventos': evento}
    return render(request, 'agenda/agenda.html', dados)

@login_required(login_url='/login/')
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if(id_evento):
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'agenda/evento.html', dados)

@login_required(login_url='/login/')
def submit_evento(request):
    if(request.POST):
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        local_evento = request.POST.get('local_evento')
        data_evento = request.POST.get('data_evento')
        data_final_evento = request.POST.get('data_final_evento')
        usuario = request.user
        
        id_evento = request.POST.get('id_evento')

        if(id_evento):
            # Evento.objects.filter(id=id_evento).update(
            #                                             titulo=titulo, 
            #                                             descricao=descricao,
            #                                             local_evento=local_evento,
            #                                             data_evento=data_evento,
            #                                             data_final_evento=data_final_evento,
            #                                           )
            evento = Evento.objects.get(id=id_evento)
            if(evento.usuario == usuario):
                evento.titulo = titulo
                evento.descricao = descricao
                evento.local_evento = local_evento
                evento.data_evento = data_evento
                evento.data_final_evento = data_final_evento
                evento.save()
        else:
            Evento.objects.create(
                                    titulo=titulo, 
                                    descricao=descricao,
                                    local_evento=local_evento,
                                    data_evento=data_evento,
                                    data_final_evento=data_final_evento,
                                    usuario=usuario
                                )
    else:
        messages.error(request, "Dados inseridos incorretamente")
    return redirect('/') 

@login_required(login_url='/login/')
def delete_evento(request,id_evento):
    usuario = request.user
    # Evento.objects.filter(id=id_evento).delete()
    evento = Evento.objects.get(id=id_evento)
    if(usuario == evento.usuario):
        evento.delete()
    return redirect('/')