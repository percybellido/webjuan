from django.db import models

class Link(models.Model):
    key=models.SlugField(verbose_name="nombre clave", max_length=100, unique=True)
    name=models.CharField(verbose_name="Red Social", max_length=200)
    url=models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name="enlace"
        verbose_name_plural="enlaces"
        ordering=['-created']

    def __str__(self):
        return self.name
