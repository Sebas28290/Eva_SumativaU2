from django.db import models

# Create your models here.


class Cliente (models.Model):
    nombre = models.CharField (max_length=50)
    rut = models.CharField (unique=True, max_length=12)
    correo = models.EmailField (unique = True, max_length=35)
    saldo = models.BigIntegerField()
    atendido = models.BooleanField ()

    def __str__ (self):
        return f"{self.nombre}"


class Atención (models.Model):
    dueño = models.ForeignKey (Cliente, on_delete=models.CASCADE)
    mascota = models.CharField (max_length=25)
    descripcion =models.TextField (max_length=300)
    precio = models.PositiveBigIntegerField  ()
    fecha = models.DateField ()
    

    def __str__ (self):

        return f"Mascota: {self.mascota} - Dueño: {self.dueño}"
    

