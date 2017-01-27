from __future__ import unicode_literals
from django.db import models

# Create your models here
class data(models.Model):

	latitude = models.FloatField()
	longitude = models.FloatField()
	
	temperature = models.IntegerField()
	humidity = models.IntegerField()
	co2 = models.IntegerField()
	smoke = models.IntegerField()

	def __str__(self):
		return str(self.latitude) + " - " + str(self.longitude)