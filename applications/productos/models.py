from django.db import models

# Create your models here.
class Producto(models.Model):
    name=models.CharField('Nombre', max_length=80)
    precio=models.DecimalField('Precio', max_digits=10, decimal_places=2)
    image=models.ImageField(verbose_name="Imagen", upload_to="products", blank=True, null=True)
    class Meta:
        verbose_name="producto"
        
    def __str__(self):
        return self.name