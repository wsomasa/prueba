from django.db import models

from django.db import models
from django.contrib.auth.models import User


class Categorias(models.Model):
    nombre= models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
        
    def __str__(self):
        
        return self.nombre 
        
class Area(models.Model):
    titulo = models.CharField(max_length=100)
    contenido=models.TextField()

    imagen=models.ImageField(upload_to='media/area', null=True, blank=True)  #indicamos que la imagene es opcional con los ultimos argumentos
    autor=models.ForeignKey(User, on_delete=models.CASCADE) #aqui indicamos que cuando se elimine el autor, elimine todos los pots que ese autor haya creado.
    cateqorias=models.ManyToManyField(Categorias) #aqui indicamos que relaciones las categorias.
    
    #created=models.DateTimeField(auto_now_add=True)
    #update=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
    