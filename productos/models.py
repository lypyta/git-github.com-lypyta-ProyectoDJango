from django.db import models

# Create your models here.
class Servicio(models.model):
    nombre_s = models.CharField(max_length=80)

class Cliente(models.model):
    nombre_c = models.CharField(max_length=80)
    tipo_cliente = models.CharField(max_length=80)
    rut = models.CharField(max_length=16)
    telefono = models.CharField(max_length=12)
    direccion = models.CharField(max_length=80)
    CantHoras = models.IntegerField()
    PrecioHora = models.IntegerField()
    Total = models.IntegerField()
    nombre_s = models.ForeignKey(Servicio, on_delete=models.PROTECT)