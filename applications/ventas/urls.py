from django.urls import path
from . import views

urlpatterns=[
    path('', views.ventas, name='ventas'),
    path(
        'lista-ventas/',
        views.ListVentas.as_view(),
        name='lista-ventas',
        ),
    path(
        'lista-pagos/',
        views.ListPagos.as_view(),
        name='lista-pagos'
    )
]