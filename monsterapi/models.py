from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

#Modelo especies
class Clase(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + ''
    
#Modelo elementos
#Se usará para definir tanto el elemento como las debilidades del monstruo
class Elemento(models.Model):
    nombre = models.CharField(max_length=50)
    icono = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.nombre + ''
    
#modelo estados+
class Estado(models.Model):
    nombre = models.CharField(max_length=50)
    icono = models.URLField(max_length=1000, blank=True, null=True)

    def __str__(self) -> str:
        return self.nombre + ''

#modelo Generacion (a que generación pertenece el monstruo)
class Generacion(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre + ''
    
#To Do: si se desea posteriormente, agregar modelo "Juegos" 
# para hacer referencia a los juegos en los cuales cada monstruo aparece

#Modelo Principal "Monstruo"
class Monstruo(models.Model):
    nombre = models.CharField(max_length=50)
    icono = models.URLField(max_length=1000, blank=True, null=True)
    #apodos = models.Model(max_length=)
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, default=None)
    elemento = models.ManyToManyField(Elemento, related_name="elemento_monstruo")
    estado = models.ManyToManyField(Estado, related_name="estados_aplicados")
    debilidad = models.ManyToManyField(Elemento, related_name= "debilidad_monstruo")
    max_size = models.FloatField(blank=False, null=False)
    min_size = models.FloatField(blank=False, null=False)
#   generacion = models.ForeignKey(Generacion, on_delete=models.CASCADE)
#   is_hidden = models.BooleanField(default=False, verbose_name='¿Está oculto?', help_text='El monstruo no se mostrará', null=False)

    #Validación para que tamaño maximo sea siempre mayor a tamaño minimo
    def clean(self):
        if self.max_size is None:
            raise ValidationError({'El campo max_size es obligatorio'})
        if self.min_size is None:
            raise ValidationError({'El campo min_size es obligatorio'})
        if self.max_size <= 0:
            raise ValidationError({'El tamaño del monstruo debe ser mayo a 0'})
        if self.min_size <= 0:
            raise ValidationError({'El tamaño del monstruo debe ser mayo a 0'})
        if self.max_size < self.min_size:
            raise ValidationError({'El campo min_size no puede ser menor que el campo max_size'})

    def __str__(self):
        return self.nombre + ''