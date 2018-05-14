from django.db import models
from django.utils import timezone
from .choices import *
from django.contrib import messages, sessions

# Create your models here. Va

class User(models.Model):
    username = models.CharField(max_length=30, help_text='Nombre de usuario', primary_key=True)
    password1 = models.CharField(max_length=30, help_text='Contraseña')
    password2 = models.CharField(max_length=30, help_text='Confirmacion de contraseña')
    first_name = models.CharField(max_length=30, help_text='Nombre')
    last_name = models.CharField(max_length=30, help_text='Apellido')
    email = models.EmailField(max_length=254, help_text='Correo electronico')

    def __str__(self):
        return self.username


class Logeado(models.Model):
    username = models.CharField(max_length=30, help_text='Nombre de usuario')
    password = models.CharField(max_length=30, help_text='Contraseña')

    def __str__(self):
        return self.username

class Recuperacion(models.Model):
    email = models.EmailField(max_length=254, help_text='Correo electronico')

    def __str__(self):
        return self.email

class Cita(models.Model):
    username = models.CharField(max_length=30, help_text='Nombre de usuario')
    hora = models.TimeField(help_text="Formato hora:minutos")
    dia = models.DateField(help_text="Formato dia/mes/año")
    email = models.EmailField(help_text='Correo electronico')
    servicio = models.CharField(max_length=25, choices=SERVICES_CHOICES2, help_text='Eliga su servicio', default='1')

    def __str__(self):
        return self.username + str(self.hora)

class Opiniones(models.Model):
    texto = models.CharField(max_length=300, default="")
    terminos = models.BooleanField(default=True)

    def __str__(self):
        return self.texto


class Producto(models.Model):
    id = models.AutoField
    idenfificador = models.CharField(max_length=2, choices=SALTO_CHOICES, help_text="4 significa un nuevo renglón de items", default='1', unique=False)
    categoria = models.CharField(max_length=25, choices=PRODUCT_CHOICES, default='1')
    nombre = models.CharField(max_length=120)
    nota = models.CharField(max_length=120)
    descripcion = models.CharField(max_length=300, default="")
    precio = models.DecimalField(decimal_places=2, max_digits=10)
    peso = models.DecimalField(decimal_places=2, max_digits=5, default=1)
    imagen = models.CharField(max_length=120)
    existencias = models.IntegerField(default=1)
    #descuento = models.DecimalField(max_digits=2, decimal_places=2, default=)

    def __str__(self):
        return  self.categoria + "/" + self.nombre

