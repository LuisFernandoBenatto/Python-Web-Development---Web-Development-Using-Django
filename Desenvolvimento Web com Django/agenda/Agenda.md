# Agenda Django
## Iniciando projeto
### Criando novo projeto Agenda
```py
    $ cd .\dev_django\
    $ .\Scripts\activate

    $ django-admin startproject agenda
    $ cd Agenda
    $ django-admin startapp core
    $ ls
    $ python manage.py runserver 9999
```
### Migrate
```py
    $ python manage.py migrate
```
#### settings.py
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
### Criando Admin para <a href="http://localhost:9999/admin/login/?next=/admin/">Django administration</a>
```py
    $ python manage.py createsuperuser
    adm
    adm@example.com
    adm12345
    
    $ python manage.py createsuperuser --username admin
    admin@admin.com
    admin12345
```
#### models.py
```py
    from django.db import models

    class Evento(models.Model):
        titulo = models.CharField(max_length=100)
        descricao = models.TextField(blank=True, null=True)
        data_evento = models.DateTimeField()
        data_final_evento = models.DateTimeField()
        data_criacao = models.DateTimeField(auto_now=True)
```
### Comando para fazer a migrations do app core
```py
    $ python manage.py makemigrations core  
```
### Sql migrate
```py
    $ python manage.py sqlmigrate core 0001
```
#### models.py
```py
    from django.db import models

    class Evento(models.Model):
        titulo = models.CharField(max_length=100)
        descricao = models.TextField(blank=True, null=True)
        data_evento = models.DateTimeField()
        data_final_evento = models.DateTimeField()
        data_criacao = models.DateTimeField(auto_now=True)

        class Meta:
            db_table = 'evento'
```
### Comando para fazer a migrations do app core
```py
    $ python manage.py makemigrations core  
```
### Sql migrate
```py
    $ python manage.py sqlmigrate core 0001
```
### Comando para subir para o banco de daods
```py
    $ python manage.py migrate core 0001
```
#### models.py
```py
    from django.db import models

    class Evento(models.Model):
        titulo = models.CharField(max_length=100)
        descricao = models.TextField(blank=True, null=True)
        data_evento = models.DateTimeField()
        data_final_evento = models.DateTimeField()
        data_criacao = models.DateTimeField(auto_now=True)

        class Meta:
            db_table = 'evento'
        def __str__(self):
            return self.titulo
```
#### admin.py
````py
    from django.contrib import admin
    from core.models import Evento
    # Register your models here.

    class EventoAdmin(admin.ModelAdmin):
        list_display = ('titulo', 'data_evento', 'data_final_evento', 'data_criacao')

    admin.site.register(Evento, EventoAdmin)
```
