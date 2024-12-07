from django.shortcuts import render
from django.views.generic import ListView

from .models import Venta, Ventas_MP

# Create your views here.
def ventas(request):
    return render(request, 'ventas/ventas.html')

class ListVentas(ListView):
    context_object_name='lista_ventas'
    template_name='ventas/lista_ventas.html'
    paginate_by=6
    ordering=['-Venta_Fecha']

    def get_queryset(self):
        
        return Venta.objects.listar_ventas()
    
class ListPagos(ListView):
    context_object_name='lista_pagos'
    template_name='ventas/lista_pagos.html'
    paginate_by=6

    def get_queryset(self):
        
        return Ventas_MP.objects.listar_pagos()