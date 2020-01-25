from django.db import models

# Create your models here.

class Persona(models.Model):
	nombre = models.CharField(max_length = 100, blank = False, verbose_name = "Nombre y Apellidos")

	Nada = ' '
	Diabético = 'Diabético'
	Celiaco = 'Celiaco'
	Lactosa = 'Intolerante a la lactosa'
	Vegetariano = 'Vegetariano'
	Vegano = 'Vegano'
	Otros = 'Otros'

	opciones = [
		(Nada, ' '),
		(Diabético, 'Diabético'),
		(Celiaco, 'Celiaco'),
		(Lactosa, 'Intolerante a la lactosa'),
		(Vegetariano, 'Vegetariano'),
		(Vegano, 'Vegano'),
		(Otros, 'Otros'),
	]

	intolerancia = models.CharField(max_length = 24, choices = opciones, default = Nada, verbose_name = "Intolerancia")
	transporte = models.BooleanField(verbose_name = "Transporte")

	def __str__(self):
		return self.nombre
