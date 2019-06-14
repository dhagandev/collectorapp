from django.db import models
import datetime

# Create your models here.
class Gem(models.Model):
	gem_type = models.CharField(max_length=100)
	color = models.CharField(max_length=100)
	location_found = models.CharField(max_length=100)
	date_found = models.DateField()

	def __str__(self):
		return self.color + " " + self.gem_type

gems = [
	Gem('Turquoise', 'Light Blue', 'Arizona', datetime.datetime(2019, 6, 9)),
	Gem('Quartz', 'Rose Pink', 'South Dakota', datetime.datetime(2019, 5, 23)),
	Gem('Ruby', 'Dark Red', 'Brazil', datetime.datetime(2019, 5, 7)),
	Gem('Malachite', 'Green', 'Mexico', datetime.datetime(2019, 4, 16))
]