from django.db import models
from django.db.models.fields import CharField, TextField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ManyToManyField

# Create your models here.

class Categoria(models.Model):
    nombre = CharField(max_length=200)

    def __str__(self) :
        return self.nombre

class Sitio(models.Model):
    nombre = CharField(max_length=250)
    descripcion = TextField()
    imagen = ImageField(upload_to='Sitios')
    ubicacion = TextField()
    categoria = ManyToManyField(Categoria)

    def __str__(self):
        return self.nombre
