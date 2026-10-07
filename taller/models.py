from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.BooleanField(default=True)
    def __str__(self):
        return self.nombre

class OrdenReparacion(models.Model):
    codigo_orden=models.CharField(max_length=20, unique=True)
    patente_vehiculo=models.CharField(max_length=8)
    modelo_vehiculo=models.CharField(max_length=100)
    cliente_nombre=models.CharField(max_length=100)
    costo_estimado=models.DecimalField(max_digits=10, decimal_places=2)
    estado=models.CharField(max_length=20, choices=[('ingresado', 'Ingresado'), ('pendiente', 'Pendiente'), ('en_proceso', 'En Proceso'), ('finalizada', 'Finalizada'), ('LISTO', 'Listo')])
    fecha_ingreso=models.DateTimeField(auto_now_add=True)
    especialidad=models.ForeignKey(especialidad, on_delete=models.CASCADE, related_name='ordenes_reparacion')
    