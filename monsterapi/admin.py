
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

#Modelo Generación
class GeneracionAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

admin.site.register(Generacion, GeneracionAdmin)

#Modelo Monstruo 
class MonstruoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'icono', 'max_size', 'min_size', 'generacion',)

    filter_horizontal = ('clase', 'elemento', 'estado', 'debilidad',)

admin.site.register(Monstruo, MonstruoAdmin)