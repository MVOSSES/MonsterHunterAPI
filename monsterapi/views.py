from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import  reverse

#importaciones para la api
from monsterapi.models import Monstruo, Clase, Elemento, Estado
from monsterapi.serializers import MonstruoSerializer, ClaseSerializer, ElementoSerializer, EstadoSerializer
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

#View todos los elementos
@api_view(['Get'])
def elementos_list(request):
    if request.method == 'GET':
        elementos = Elemento.objects.all()
        serializer = ElementoSerializer(elementos, many=True)
        return Response(serializer.data)
    
#View buscar Elementos por ID
@api_view(['GET'])
def elementos_detail(request, pk):
    try:
        elementos = Elemento.objects.get(pk=pk)
    except Elemento.DoesNotExist:
        return Response({"error": "Elemento no encontrada"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ElementoSerializer(elementos)
        return Response(serializer.data)

#View buscar por nombre
@api_view(['GET'])
def elementos_por_nombre(request, nombre):
    try:
        elementos = Elemento.objects.get(nombre=nombre)
    except Elemento.DoesNotExist:
        return Response({"error": "Elemento no encontrado"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ElementoSerializer(elementos)
        return Response(serializer.data)
    
#Fin views Elementos

"""
Views Estados 
Este apartado contiene las api_views para solicitar los datos de las Estados
"""

#View todos los Estados
@api_view(['GET'])
def estados_list(request):
    if request.method == 'GET':
        estados = Estado.objects.all()
        serializer = EstadoSerializer(estados, many=True)
        return Response(serializer.data)
    
#View buscar Estado por nombre
@api_view(['GET'])
def estados_detail(request, pk):
    try:
        estados = Estado.objects.get(pk=pk)
    except Estado.DoesNotExist:
        return Response({'error': 'Estado no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EstadoSerializer(estados)
        return Response(serializer.data)
    
#View buscar Estado por nombre
@api_view(['GET'])
def estados_por_nombre(request, nombre):
    try:
        estados = Estado.objects.get(nombre=nombre)
    except Estado.DoesNotExist:
        return Response({'error':'Estado no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = EstadoSerializer(estados)
        return Response(serializer.data)

#Fin views Estados