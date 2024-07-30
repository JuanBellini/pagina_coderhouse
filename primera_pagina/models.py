from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Libro(models.Model):
    titulo =models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    fecha_publicacion = models.DateField

    def __str__(self):
        return self.titulo
    
class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    libros = models.ManyToManyField(Libro)

    def __str__(self):
        return self.nombre

