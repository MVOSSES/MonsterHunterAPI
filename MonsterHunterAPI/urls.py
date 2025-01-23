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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('monstruosDATA/', monstruos_list, name='monstruosDATA'),
    path('monstruosDATA/<int:pk>/', monstruo_detail, name='monstruosDATA'),
    path('monstruosDATA/<str:nombre>/',monstruo_por_nombre, name='monstruosDATA'),
    path('clasesDATA/',clases_list, name='clasesDATA'),
    path('clasesDATA/<int:pk>/',clases_detail,name='clasesDATA'),
    path('clasesDATA/<str:nombre>/',clase_por_nombre,name='clasesDATA'),
]
