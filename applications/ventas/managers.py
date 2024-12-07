from django.db import models
from django.db.models import Sum, F

class VentaManagers(models.Manager):
    
    def listar_ventas(self):
        return self.all()

class Venta_MPManagers(models.Manager):
    def listar_pagos(self):
        return self.all()