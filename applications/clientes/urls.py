from django.urls import path
from . import views

urlpatterns=[
    path(
        '',
        views.ClientesView.as_view(),
        name='clientes',
        ),
    
    path(
        'lista-clientes/',
        views.ListClientes.as_view(),
        name='lista-clientes',
        ),

    path(
        'lista-ventasT/',
        views.ListVentasCliente.as_view(),
        name='lista-ventasT',
        ),

    path(
        'lista-pagosT/',
        views.ListPagosCliente.as_view(),
        name='lista-pagosT',
        ),
    
    path(
        'lista-saldos/',
        views.ListSaldosCliente.as_view(),
        name='lista-saldos',
        ),
    path(
        'ver-cliente/<pk>/', views.ClienteDetailView.as_view(),
        name='cliente-detalle'
    )
    ]