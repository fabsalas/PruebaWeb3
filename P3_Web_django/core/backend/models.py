from django.db import models

# Create your models here.

# Tabla componente y sus atributos
class Componente(models.Model):
     id     = models.AutoField(primary_key=True)
     nombre = models.CharField(max_length=99,)

     def __str__(self):
         return  'Nombre: ' +self.nombre
         #return  self.nombre

# Tabla Fabricante y sus atributos
class Fabricante(models.Model):
    id     = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=99,)

    def __str__(self):
        return self.nombre
    
# Tabla Producto y sus atributos
class Producto(models.Model):
    id          = models.AutoField(primary_key=True)
    nombre      = models.CharField(max_length=99,)
    fabricante  = models.ForeignKey(Fabricante, on_delete=models.CASCADE, null=True, blank=True)
    componente  = models.ForeignKey(Componente, on_delete=models.CASCADE, null=True, blank=True)
    precio      = models.IntegerField(default=0)
    stock       = models.IntegerField(default=0)
    imagen      = models.ImageField(upload_to=0, null=True, blank=True)

