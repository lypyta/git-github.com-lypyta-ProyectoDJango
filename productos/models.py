from django.db import models

# Create your models here.
class Servicio(models.Model):
    nombre_s = models.CharField(max_length=80) 
       
class Cliente(models.Model):
    nombre_c = models.CharField(max_length=80)
    tipo_cliente = models.CharField(max_length=80)
    rut = models.CharField(max_length=16)
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=80)
    CantHoras = models.IntegerField()
    PrecioHora = models.IntegerField()
    Total = models.IntegerField()
    nombre_s = models.ForeignKey(Servicio, on_delete=models.PROTECT)

from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class ItemCarrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)