from django.db import models

# Create your models here.


class Producto(models.Model):
    name = models.CharField(max_length=64)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=128)
    imagen = models.ImageField(
        upload_to='img', null=True, blank=True)

    def __str__(self):
        return f'{self.name} -> {self.precio}'
