from django.db import models

from .managers import ClienteManager

# Create your models here.

class Cliente(models.Model):
    name=models.CharField('Nombre', max_length=80)
    status=models.SmallIntegerField('Estado', default=1, null=True)
    phone=models.IntegerField('Telefono', null=True, blank=True)
    email=models.EmailField('Email', null=True, blank=True)
    objects=ClienteManager()
    
    class Meta:
        verbose_name='Cliente'
        ordering=['name']

    def __str__(self):
        return self.name
