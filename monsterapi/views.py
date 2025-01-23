from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import  reverse

#importaciones para la api
from monsterapi.models import Monstruo, Clase
from monsterapi.serializers import MonstruoSerializer, ClaseSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
#Views API

"""
Views monstruos
Este apartado contiene las api_views para solicitar los datos de las monstruos
"""

#views api con interfaz de rest framework
#View todos los monstruos
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
        return Response({"error": "Monstruo no encontrada"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MonstruoSerializer(monstruo)
        return Response(serializer.data)
    
#Experimento api buscar elemento por el nombre / Exitoso
@api_view(['GET'])
def monstruo_por_nombre(request, nombre):
    try:
        monstruo = Monstruo.objects.get(nombre=nombre)
    except Monstruo.DoesNotExist:
        return Response({"error": "Monstruo no encontrada"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = MonstruoSerializer(monstruo)
        return Response(serializer.data)                        
    
#Fin Views Monstruos

"""
Views Clases 
Este apartado contiene las api_views para solicitar los datos de las clases
"""

#View todas las clases
@api_view(['GET'])
def clases_list(request):
    if request.method == 'GET':
        clases = Clase.objects.all()
        serializer = ClaseSerializer(clases, many=True)
        return Response(serializer.data)
    
#View buscar Clase por ID
@api_view(['GET'])
def clases_detail(request,pk):
    try:
        clases = Clase.objects.get(pk=pk)
    except Clase.DoesNotExist:
        return Response({"error": "Clase no encontrada"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ClaseSerializer(clases)
        return Response(serializer.data)
    
@api_view(['GET'])
def clase_por_nombre(request,nombre):
    try:
        clases = Clase.objects.get(nombre=nombre)
    except Clase.DoesNotExist:
        return Response({"error": "Clase no encontrada"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ClaseSerializer(clases)
        return Response(serializer.data)
    
#Fin Views Clases

"""
Views Elementos
Este apartado contiene las api_views para solicitar los datos de las Elementos
"""

#Fin views Elementos

"""
Views Estados 
Este apartado contiene las api_views para solicitar los datos de las Estados
"""

#Fin views Estados