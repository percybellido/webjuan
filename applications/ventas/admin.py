from django.contrib import admin
from .models import Venta, Ventas_MP, VentaDetalle, MetodosPago

class Ventas_MPAdmin(admin.ModelAdmin):
    list_display=('VentasMP_Ventas_Id', 'VentasMP_Fecha', 'VentasMP_MP_Id', 'VentasMP_Total')
    search_fields=('VentasMP_Ventas_Id_Venta_CliId', 'VentasMP_Fecha', 'VentasMP_MP_Id', 'VentasMP_Total')

admin.site.register(Venta)
admin.site.register(VentaDetalle)
admin.site.register(MetodosPago)
admin.site.register(Ventas_MP)
