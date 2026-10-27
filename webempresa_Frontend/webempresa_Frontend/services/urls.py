from django.urls import path
from . import views

urlpatterns = [
    path('', views.services, name='services'),
    path('blog/', views.blog, name='blog'), # Agregamos la ruta del blog
]