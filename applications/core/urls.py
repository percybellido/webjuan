from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('productos/', views.productos, name='productos'),
    path('clientes/', views.clientes, name='clientes'),
    path('ventas/', views.ventas, name='ventas'),
    path('blog/', views.blog, name='blog'),
    path('contacto/', views.contacto, name='contacto'),
]