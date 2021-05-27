from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

ENTIDAD = [
    ("EPS","EPS"),
    ("IPS","IPS"),
    ("ARL","ARL"),
]

class User(AbstractUser):
    cedula = models.IntegerField(verbose_name="Cédula",blank=True, null=True)
    imagen = models.ImageField(max_length=200,upload_to="images/",verbose_name="Imagen de perfil",blank=True, null=True)
    pais = models.CharField(max_length=100,verbose_name="País",blank=True, null=True)
    entidad = models.CharField(max_length=50, verbose_name="Entidad",blank=True, null=True,choices = ENTIDAD)
