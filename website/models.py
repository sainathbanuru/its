from __future__ import unicode_literals
from django.db import models

# Create your models here
class data(models.Model):

	temperature = models.IntegerField()
	humidity = models.IntegerField()
	co2 = models.IntegerField()
	smoke = models.IntegerField()
	
	latitude = models.FloatField()
	longitude = models.FloatField()

	# If 1 our own data, 2 implies from another source..
	source = models.IntegerField(default=0)

	# Hardware id
	h_id = models.IntegerField(default=0)

	# Time
	year = models.IntegerField(default=2017)
	month = models.IntegerField(default=3)
	day = models.IntegerField(default=30)
	hour = models.IntegerField(default=0)

	
	def __str__(self):
		return str(self.latitude) + " - " + str(self.longitude)