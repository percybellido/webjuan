from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

from django.views.generic import ListView, TemplateView, DetailView

from .models import Cliente

# Create your views here.
class ClientesView(TemplateView):
    template_name='clientes/clientes.html'

class ListClientes(ListView):
    context_object_name='lista_clientes'
    template_name='clientes/lista_clientes.html'
    paginate_by=6

    def get_queryset(self):
        palabra_clave=self.request.GET.get('kword', '')
        return Cliente.objects.buscar_cliente(palabra_clave)
    
class ListVentasCliente(ListView):
    context_object_name='lista_ventas'
    template_name='clientes/lista_ventas.html'
    paginate_by=6

    def get_queryset(self):
        return Cliente.objects.ventas_totales_cliente()
    
class ListPagosCliente(ListView):
    context_object_name='lista_pagos'
    template_name='clientes/lista_pagos.html'
    paginate_by=6

    def get_queryset(self):
        return Cliente.objects.pagos_totales_cliente()
    
class ListSaldosCliente(ListView):
    context_object_name='lista_saldos'
    template_name='clientes/lista_saldos.html'
    paginate_by=6

    def get_queryset(self):
        return Cliente.objects.saldos_totales()
    
class ClienteDetailView(DetailView):
    model=Cliente
    template_name='cliente/detail_cliente.html'

    def get_context_data(self, **kwargs):
        context=super(ClienteDetailView, self).get_context_data(**kwargs)

        return context