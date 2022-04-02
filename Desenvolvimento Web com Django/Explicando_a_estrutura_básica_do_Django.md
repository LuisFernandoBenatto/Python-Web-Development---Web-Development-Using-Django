# Agenda

## • DJANGO-ADMIN
### DJANFO-ADMIN.PY
> • É o utilitário de linha de comando do Django para tarefas administrativas

## • MANAGE
> • É um wrapper em volta do django-admin.py

> • Ele delega tarefas para o django-admin.py

> • Responsável por colocar o pacote do no sys.path

> • Ele define a variável de ambiente DJANGO_SETTINGS_MODULE que então aponta para o arquivo settings.py

> • Por isso, o manage.py é gerado automaticamente junto ao projeto, para facilitar a uso de comandos do django-admin.py (comandos administrativos) 

## • WSGI
> • Web Server Gatewy Interface - Interface de porta de entrada do servidor web

> • Plataforma padrão para aplicação web em Python

> • Serve de interface do servidor Web e a Aplicação Web 

> • O Django com o comando *startproject* inicia uma configuração WSGI padrão para que se possa executar sua aplicação web

> • Quando se inicia a aplicação Django com o comando *runserver* é iniciado um servidor de aplicação web leve. Esse servidor é especificada pela configuração WSGI_APPLICATION

## • SETTINGS
> • É responsável pelas configurações do Django

> • Nele é possível configurar por exemplo apps, conexão com banco de dados, templates, time zone, cache, segurança, arquivos estáticos, etc.

## • URLS
> • É um Schema de URL

> • Responsável por gerenciar as Rotas da URLs, onde é possível configurar para onde cada rota será executada

> • É um forma limpa e elegante para gernciar URLs

## • VIEWS
> • Responsável por processar e retornar uma resposta para o cliente que fez a requisição

## • MODELS
> • Define o modelo de dados inteiramente em Python

> • Faz a abstração dos objetos de banco para o Python, transformando todas as tabelas em classes e os acessos são feito utilizando linguagem Python, onde o Django reliza a transformação para SQL

```py
    class Pessoa(models.Model):
        name = models.CharField(max_length=200)
        idade = models.IntegerField()

    pessoa = Pessoa.objects.get(nome="Rafael")

```
```sql
    select * from pessoa where nome = 'Rafael';
```
## • ADMIN
> • Interface administrativa gerada automaticamente pelo Django

> • Ele lê os metadados que estão nos models e fornece uma interface poderosa e pronta para manipulação de dados

```py
    from django.contrab import admin
    from core.models import Pessoa

    class PessoaAdmin(admin.ModelAdmin):
        list_display = ('nome', 'idade')
        list_filter = ('nome',)
    
    admin.site.register(Pessoa)
```

## • STATIC
> • Responsável por armazenar os arquviso estáticos

> • CSS, JavaScript, imagens

## • TEMPLATES
> • Responsável por armazenar os arquivos HTML

> • O diretório templates é diretório padrão para armazenarmos todo o conteúdo HTML da nossa aplicação