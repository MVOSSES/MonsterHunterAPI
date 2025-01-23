
from django.contrib import admin
from monsterapi.models import Clase,Elemento,Estado,Generacion,Monstruo
# Register your models here.

#Crear clases para que el administrador pueda realizar inserciones y ediciones en la base de datos

#Modelo Clase
class ClaseAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Clase, ClaseAdmin)

#Modelo Elemento
class ElementoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'icono',)

admin.site.register(Elemento, ElementoAdmin)

#Modelo Estado
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'icono',)

admin.site.register(Estado, EstadoAdmin)

""" Se eliminó el modelo generación ya que no se utilizará

class GeneracionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Generacion, GeneracionAdmin)"""

#Modelo Monstruo 
class MonstruoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'icono', 'imagen', 'clase',  'max_size', 'min_size',)

    filter_horizontal = ('elemento', 'estado', 'debilidad',)

admin.site.register(Monstruo, MonstruoAdmin)