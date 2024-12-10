from django.db import models
from applications.clientes.models import Cliente
from .managers import VentaManagers, Venta_MPManagers
# Create your models here.
class Venta(models.Model):
    Venta_Fecha=models.DateTimeField('Fecha de Venta', auto_now_add=True)
    Venta_CliId=models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cliente_venta')
    Venta_NroFact=models.IntegerField('Numero de Boleta', null=True, blank=True )
    Venta_Total=models.DecimalField('Total', max_digits=10, decimal_places=2)
    objects=VentaManagers()

    class Meta:
        verbose_name='Ventas'
        ordering=['-Venta_CliId']

    def __str__(self):
        return str(self.Venta_CliId)
    
class VentaDetalle(models.Model):
    VD_VentasId=models.ForeignKey(Venta, on_delete=models.CASCADE)
    VD_Cantidad=models.IntegerField('Cajas', default=0)
    VD_Precio=models.DecimalField('Precio', max_digits=10, decimal_places=2)
    

    class Meta:
        verbose_name='Detalle de Ventas'
        ordering=['VD_VentasId']

    def __str__(self):
        return str(self.VD_VentasId)+'--'+str(self.VD_Cantidad)+'--'+str(self.VD_Precio)

class MetodosPago(models.Model):
    description=models.CharField('Metodos Pago', max_length=50, null=True)
    status=models.IntegerField(null=True, default=1)

    class Meta:
        verbose_name='Metodos de Pago'

    def __str__(self):
        return self.description

class Ventas_MP(models.Model):
    VentasMP_Ventas_Id=models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='metodos_pago')
    VentasMP_Fecha=models.DateTimeField('Fecha de Pago', auto_now_add=True)
    VentasMP_MP_Id=models.ForeignKey(MetodosPago, on_delete=models.CASCADE)
    VentasMP_Total=models.DecimalField('Subtotal', max_digits=10, decimal_places=2)
    objects=Venta_MPManagers()

    class Meta:
        verbose_name='Amortizaciones'
        ordering=['-VentasMP_Ventas_Id']

    def __str__(self):
        return str((self.VentasMP_Ventas_Id))+'--'+str(self.VentasMP_Total)+'--'+'--'+str(self.VentasMP_MP_Id)+str(self.VentasMP_Fecha)