from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User  # Importamos el modelo de usuario de Django


# Modelo para los Servicios
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="services")

    # Campos de auditoría requeridos
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['-created']

    def __str__(self):
        return self.title


# Modelo para el Blog (Post)
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)

    # Relación con el usuario que lo creó (como pidió el ingeniero)
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)

    # Categorías (puedes relacionarlo con otro modelo de categorías luego si quieres)
    categories = models.CharField(max_length=200, verbose_name="Categorías", default="General")

    # Campos de auditoría requeridos
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ['-created']

    def __str__(self):
        return self.title