from turtle import mode
from django.db import models

# Create your models here.

class Profesor(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    asignatura = models.CharField(max_length=40)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    curso = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.dni} "


class Maestranza(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    dni = models.IntegerField()
    sector = models.IntegerField()
