from django.db import models

# Create your models here.

class Tienda(models.Model):
    nombreTienda = models.CharField(max_length=32, blank=True, null=True)
    direccion = models.CharField(max_length=32, blank=True, null=True)
    provincia = models.CharField(max_length=32, blank=True, null=True)
    region = models.CharField(max_length=32, blank=True, null=True)
    fechaCreacion = models.CharField(max_length=32, blank=True, null=True)
    telefonoContacto = models.CharField(max_length=32, blank=True, null=True)


class Producto(models.Model):
    nombreProducto = models.CharField(max_length=32, blank=True, null=True)
    descripcion = models.CharField(max_length=32, blank=True, null=True)
    codigoProducto = models.CharField(max_length=32, blank=True, null=True)
    precioVenta = models.CharField(max_length=32, blank=True, null=True)
    cantidad = models.CharField(max_length=32, blank=True, null=True)
    tiendaR = models.ForeignKey(Tienda, on_delete=models.SET_NULL, blank=True, null=True)



