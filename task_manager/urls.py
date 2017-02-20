"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.http import HttpResponse

def teste(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def sobre(request, argumento):
    return HttpResponse("sobre " + str(argumento))

def tarefas(request, ano, mes):
    return HttpResponse("Tarefas de "+ str(ano) + " e mes" + str(mes))

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'home', teste),
    url(r'^sobre/([0-9]{4})/$', sobre),
    url(r'^tarefas/(?P<ano>[0-9]{4})/(?P<mes>[0-9]{2})/', tarefas)
]
