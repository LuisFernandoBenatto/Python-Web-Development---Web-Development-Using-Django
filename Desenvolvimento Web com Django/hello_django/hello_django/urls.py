"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
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
    path('soma/<int:valor_a>/<int:valor_b>/', views.soma),
    path('subtracao/<int:valor_a>/<int:valor_b>/', views.subtracao),
    path('multiplicacao/<int:valor_a>/<int:valor_b>/', views.multiplicacao),
    path('divisao/<int:valor_a>/<int:valor_b>/', views.divisao),
    path('resto/<int:valor_a>/<int:valor_b>/', views.resto),
]
