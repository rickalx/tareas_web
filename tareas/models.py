from django.db import models
from django.utils import timezone

# Create your models here.

class Tareas(models.Model):
    titulo = models.CharField(max_length=100)
    detalles = models.TextField()
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo