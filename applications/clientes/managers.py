from django.db import models
from django.db.models import Sum, F

class ClienteManager(models.Manager):
    
    def listar_clientes(self):
        return self.all()
    
    def buscar_cliente(self, kword):
        resultado=self.filter(
            name__icontains=kword
        )
        return resultado
        
    def ventas_totales_cliente(self):
        resultado=self.annotate(
            ventas_clientes=Sum('cliente_venta__Venta_Total')
        )

        for r in resultado:
            print('******')
            print(r, r.ventas_clientes)

        return resultado
    
    def pagos_totales_cliente(self):
        resultado1=self.annotate(
            pagos_clientes=Sum('cliente_venta__metodos_pago__VentasMP_Total')
        )

        for r in resultado1:
            print('*******')
            print(r, r.pagos_clientes)
        
        return resultado1
    
    def saldos_totales(self):
        resultado=self.annotate(
            pagos_realizados=Sum('cliente_venta__metodos_pago__VentasMP_Total'),

            ventas_clientes1=Sum('cliente_venta__Venta_Total', distinct=True),

            saldos_clientes=F('ventas_clientes1')-F('pagos_realizados')
        )

        for r in resultado:
            print('*******')
            print(r, r.ventas_clientes1, r.pagos_realizados, r.saldos_clientes)

        return resultado    
