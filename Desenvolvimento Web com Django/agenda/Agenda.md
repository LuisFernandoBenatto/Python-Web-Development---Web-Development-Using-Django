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
### Criando Admin para <a href="http://localhost:9999/admin/login/?next=/admin/">Django administration</a>
```py
    $ python manage.py createsuperuser
    adm
    adm@example.com
    adm12345
    
    $ python manage.py createsuperuser --username admin

```