from django.db import models

# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField(max_length=60)
    categoria = models.CharField(max_length=60)
    precio_compra = models.FloatField()
    precio_venta = models.FloatField()

class Cliente(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60) 
    telefono = models.CharField(max_length=15)

class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    articulo = models.CharField(max_length=60) 
    cantidad = models.IntegerField()

class Compra(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    distribuidor = models.CharField(max_length=60)
    articulo = models.CharField(max_length=60) 
    cantidad = models.IntegerField()

