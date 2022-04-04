from django.shortcuts import render, redirect, HttpResponse
from core.models import Evento

# Create your views here.

def hello(request):
    return HttpResponse("<h1>Hello, World</h1>")

# def index(request):
#     return redirect('/agenda/')

def lista_eventos(request):
    # usuario = request.user
    # evento = Evento.objects.get(id=1)
    evento = Evento.objects.all()
    # evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda/agenda.html', dados)