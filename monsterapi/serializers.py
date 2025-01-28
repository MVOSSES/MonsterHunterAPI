from rest_framework import serializers
from monsterapi.models import Monstruo,Clase,Elemento,Estado

#crear serializadores para que se muestren en el archivo json entregado por la api

#Serializador Clase
class ClaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ['id', 'nombre',]

#Serializador Elemento
class ElementoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elemento
        fields = ['id', 'nombre', 'icono',]

#serializador Estado
class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['id', 'nombre', 'icono',]

#Clase serializador para el modelo Monstruo
class MonstruoSerializer(serializers.ModelSerializer):
    #Agregamos los nuevos serializadores para que el archivo JSON de monstruo muestre todos los datos de los elementos referenciados y no solo el id
    clase = ClaseSerializer()
    elemento = ElementoSerializer(many=True)
    estado = EstadoSerializer(many=True)
    debilidad = ElementoSerializer(many=True)
    class Meta:
        model = Monstruo
        #en fields agregamos todos los campos que queremos que nuestro serializador procese al convertir nuestro modelo en un objeto JSON
        fields = ['id', 'nombre', 'icono', 'imagen', 'clase', 'elemento', 'estado', 'debilidad', 'max_size', 'min_size',]

        """En el serializador volveremos a realizar las validaciones para el tamaño del monstruo.
        para este proyecto el proceso es opcional, ya que la api solo contará con el metodo GET.
        en caso de que la api cuente con otros metodos como POST, PUT O DELETE la validación se debe
        realizar obligatoriamente para que coincida con las validaciones establecidas en el modelo original"""
        

#Serializers ver 2
class ClaseSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = ['id','nombre',]
class ElementoSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Elemento
        fields = ['id', 'nombre',]

class EstadoSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['id', 'nombre',]

class MonstruoSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Monstruo
        fields = ['id', 'nombre',]