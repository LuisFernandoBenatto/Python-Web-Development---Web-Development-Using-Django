from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    # return HttpResponse("<h1>Hello, World</h1>")
    # return HttpResponse("<h1>Hello, {}</h1>".format(nome))
    return HttpResponse("<h1>Hello, {} de {} anos</h1>".format(nome, idade))

def soma(request, valor_a, valor_b):
    result = valor_a + valor_b
    return HttpResponse("<h1>Soma: {} + {} = {}</h1>".format(valor_a, valor_b, result))

def subtracao(request, valor_a, valor_b):
    result = valor_a - valor_b
    return HttpResponse("<h1>Subtração: {} - {} = {}</h1>".format(valor_a, valor_b, result))

def multiplicacao(request, valor_a, valor_b):
    result = valor_a * valor_b
    return HttpResponse("<h1>Multiplicação: {} * {} = {}</h1>".format(valor_a, valor_b, result))

def divisao(request, valor_a, valor_b):
    result = valor_a / valor_b
    return HttpResponse("<h1>Divisão: {} / {} = {}</h1>".format(valor_a, valor_b, result))

def resto(request, valor_a, valor_b):
    result = valor_a % valor_b
    return HttpResponse("<h1>Resto: {} % {} = {}</h1>".format(valor_a, valor_b, result))
