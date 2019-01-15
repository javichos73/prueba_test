"""
docstring
"""
from datetime import datetime
from django.db import models


# Create your models here.


class Persona(models.Model):
    """
    Elemento esencial de persona
    """
    numero_de_documento = models.CharField(max_length=20, unique=True)
    numero_de_libreta_militar = models.CharField(max_length=20, blank=True, null=True)
    primer_apellido = models.CharField(max_length=140)
    segundo_apellido = models.CharField(max_length=140, blank=True)
    primer_nombre = models.CharField(max_length=140)
    segundo_nombre = models.CharField(max_length=140, blank=True)
    fecha_de_nacimiento = models.DateField(blank=True, null=True, help_text='(aaaa-MM-dd)')

    class Meta:
        ordering = ['primer_apellido', 'segundo_apellido']

    def __str__(self):
        return "%s %s %s" % (self.primer_apellido, self.segundo_apellido, self.primer_nombre)

    def edad(self):
        if not self.fecha_de_nacimiento:
            return None
        fecha = self.fecha_de_nacimiento.year
        hoy = datetime.date.today().year
        if datetime.date.today().month > self.fecha_de_nacimiento.month:
            return hoy - fecha
        return hoy - fecha - 1
