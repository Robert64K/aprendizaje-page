from django.db import models
from django.utils import timezone

# Create your models here.
class pages(models.Model):
	"""Registro de todas las paginas del sitio para el buscador de temas."""
	titulo = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=200)
	imagen = models.CharField(max_length=200,default='assets/img/attach-blue.png')
	urlname = models.CharField(max_length=200,default='home')
	fecha_creacion = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.titulo


		