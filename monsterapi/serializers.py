from rest_framework import serializers
from monsterapi.models import Monstruo

#Clase del serializador para el modelo Monstruo
class MonstruoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monstruo
        #en fields agregamos todos los campos que queremos que nuestro serializador procese al convertir nuestro modelo en un objeto JSON
        fields = ['id', 'nombre', 'icono', 'clase', 'elemento', 'estado', 'debilidad', 'max_size', 'min_size',]

        """En el serializador volveremos a realizar las validaciones para el tamaño del monstruo.
        para este proyecto el proceso es opcional, ya que la api solo contará con el metodo GET.
        en caso de que la api cuente con otros metodos como POST, PUT O DELETE la validación se debe
        realizar obligatoriamente para que coincida con las validaciones establecidas en el modelo original"""
        