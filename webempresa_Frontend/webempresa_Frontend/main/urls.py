from django.urls import path
from . import views

urlpatterns = [
    # El parámetro 'name' es el que Django busca cuando usas {% url '...' %} en el HTML
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('store/', views.store, name='store'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
]