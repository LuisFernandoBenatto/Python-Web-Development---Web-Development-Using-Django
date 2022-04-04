# Desenvolviento Web com Django

## Passo a passo
### Primeiros comandos (Windows PowerShell):
```py
    Inicialmente criar a Virtual env, nesse caso chamda dev_django
    $ python -m venv dev_django
    $ cd .\dev_django\
    $ .\Scripts\activate 
    Instalar o django com pip
    $ pip freeze
    $ pip install django
    $ cd ..
    $ pip freeze

    Startar o projeto chamado hello_django
    $ django-admin startproject hello_django

    Statar o app chamado core
    $ django-admin startapp core

    Subir o servidor
    $ python manage.py runserver 9999
```
#### hello_django/settings.py
    Adicionar o novo projeto
```py
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'core',
    ]
```
#### code/views.py
    Criar a View
```py
    from django.shortcuts import render, HttpResponse

    # Create your views here.

    def hello(request, nome, idade):
        # return HttpResponse("<h1>Hello, World</h1>")
        # return HttpResponse("<h1>Hello, {}</h1>".format(nome))
        return HttpResponse("<h1>Hello, {} de {} anos</h1>".format(nome, idade))
```
#### hello_django/urls.py
    Criar uma nova rota para apresentar a view
```py
    from django.contrib import admin
    from django.urls import path
    from core import views

    urlpatterns = [
        path('admin/', admin.site.urls),
        # path('', views.hello),
        # path('hello/', views.hello),
        # http://127.0.0.1:9999/hello/
        # path('hello/<nome>/', views.hello),
        # http://127.0.0.1:9999/hello/Luis/
        path('hello/<nome>/<int:idade>/', views.hello),
        # http://127.0.0.1:9999/hello/Luis/22/
    ]
```

