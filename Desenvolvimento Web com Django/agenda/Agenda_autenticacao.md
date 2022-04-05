# Agenda

## Autenticação, Login e Decoradores

### • Pacote de autenticação do Django
> • O Django já possui um pacote de autenticação que é empacotado em *django.contrib.auth*

> • Esse pacote cria as tabelas de usuário e permissões, onde fica mais fácil controlar as autenticações e permissões

> • Para se utilizar da autenticação padrão do Django é necessário que o pacote esteja entre os Apps instalados no settings do projeto (essa configuração já vem pronta por default)
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
### • Funções authenticate, login, logout, message, login, login_required
#### authenticate
> • A função authenticate do pacote django.contrib.auth é responsável por autenticar o usuário.

Importação
```py
    from django.contrib.auth import authenticate
```
Utilização
```py
    user = authenticate(username=username, password=password)
```
#### login
> • A função login do pacote django.contrib.auth é responsável por criar uma sessão para o usuário autenticado

Importação
```py
    from django.contrib.auth import login
```
Utilização
```py
    login(resquest, user)
```
#### logout
> • A função logout do pacote django.contrib.auth é responsável por limpar os dados do usuário da sessão

Importação
```py
    from django.contrib.auth import authenticate, login, logout
```
Utilização
```py
    user = logout(resquest)
```
#### login_required
> • A função login_required do pacote django.contrib.auth é responsável por autenticar o usuário

> • Ela é decorador que é utilizado em todas as funções/views que necessitam de um usuário logado/autenticado para serem acessadas

Importação
```py
    from django.contrib.auth.decorators import login_required
```
Utilização
```py
    @login_required(login_url='/login/')
    def lista_eventos(request):
```
### • Decoradores
> • São funções que são usadas sobre outras funções.

> • Os decoradores são usados para extrair um código comum que deve ser aplicado para diversas funções.

> • A função login_required do pacote django.contrib.auth por exemplo, usada como decorador, faz com que seja realizada uma validação comum (usuário logado) para que em caso de usuário não logado, impeça a execução da função a qual ela está decorando.

### • Implementação login
### • Implementação logout
