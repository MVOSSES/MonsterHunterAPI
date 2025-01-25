"""
URL configuration for MonsterHunterAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from monsterapi.views import monstruos_list, monstruo_detail, monstruo_por_nombre
from monsterapi.views import clases_list, clases_detail, clase_por_nombre
from monsterapi.views import elementos_list, elementos_detail, elementos_por_nombre
from monsterapi.views import estados_list, estados_detail, estados_por_nombre, ver_todo
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mhapi/', ver_todo, name='mhapi'),
    path('mhapi/monstruos/', monstruos_list, name='monstruos'),
    path('mhapi/monstruos/<int:pk>/', monstruo_detail, name='monstruos'),
    path('mhapi/monstruos/<str:nombre>/',monstruo_por_nombre, name='monstruos'),
    path('mhapi/clases/',clases_list, name='clases'),
    path('mhapi/clases/<int:pk>/',clases_detail,name='clases'),
    path('mhapi/clases/<str:nombre>/',clase_por_nombre,name='clases'),
    path('mhapi/elementos/', elementos_list, name='elementos'),
    path('mhapi/elementos/<int:pk>/', elementos_detail, name='elementos'),
    path('mhapi/elementos/<str:nombre>/', elementos_por_nombre, name='elementos'),
    path('mhapi/estados/', estados_list, name='estados'),
    path('mhapi/estados/<int:pk>/', estados_detail, name= 'estados'),
    path('mhapi/estados/<str:nombre>/', estados_por_nombre, name='estados'),
    path('',TemplateView.as_view(template_name="index.html"),name="index"),
    path('docs/',TemplateView.as_view(template_name="monsterapi/docs.html"),name="docs"),
    path('about/',TemplateView.as_view(template_name="monsterapi/about.html"),name="about"),
]
