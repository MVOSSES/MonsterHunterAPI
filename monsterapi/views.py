from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import  reverse

#importaciones para la api
from monsterapi.models import Monstruo
from monsterapi.serializers import MonstruoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
#Views API
#views api con interfaz de rest framework
@api_view(['GET'])
def monstruos_list(request):
    if request.method == 'GET':
        monstruos = Monstruo.objects.all()
        serializer = MonstruoSerializer(monstruos, many=True)
        return Response(serializer.data)

#View api buscar por id
@api_view(['GET'])
def monstruo_detail(request, pk):
    try:
        monstruo = Monstruo.objects.get(pk=pk)
    except Monstruo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MonstruoSerializer(monstruo)
        return Response(serializer.data)
    
#Experimento api buscar elemento por el nombre / Exitoso
@api_view(['GET'])
def monstruo_por_nombre(request, nombre):
    try:
        monstruo = Monstruo.objects.get(nombre=nombre)
    except Monstruo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MonstruoSerializer(monstruo)
        return Response(serializer.data)                        
    
#