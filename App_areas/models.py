from django.db import models
from django.contrib.auth.models import User

        
class Areas(models.Model):
    especialidad = models.CharField(max_length=100)
    contenido=models.TextField()
    imagen=models.ImageField(upload_to='media/areas', null=True, blank=True)  
    
    class Meta:
        verbose_name='area'
        verbose_name_plural='areas'

    def __str__(self):
        return f"{self.especialidad} - {self.contenido}"