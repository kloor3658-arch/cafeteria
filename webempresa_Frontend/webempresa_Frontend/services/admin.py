from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Service, Post

# Configuración para el modelo Service
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated') # Hace que los campos de auditoría sean de solo lectura

# Configuración para el modelo Post (Blog)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# Registramos los modelos
admin.site.register(Service, ServiceAdmin)
admin.site.register(Post, PostAdmin)