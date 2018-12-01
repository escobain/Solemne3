from django.db import models

# Create your models here.

class Adoptante(models.Model):
    correo = models.CharField(max_length=100)
    run = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100)
    fecha_n = models.DateField(auto_now_add=True)
    telefono = models.IntegerField()
    region = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    tipo_vivienda = models.CharField(max_length=100)


    def __str__(self):
        return "{0}{1}".format(self.run, self.nombre)
    

