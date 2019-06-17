from django.db import models
from django.urls import reverse
import datetime

STATUS_ENUM = (
	('A', 'Available'),
	('S', 'Sold'),
	('P', 'Sale Pending')
)

# Create your models here.
class Gem(models.Model):
	gem_type = models.CharField(max_length=100)
	color = models.CharField(max_length=100)
	location_found = models.CharField(max_length=100)
	date_found = models.DateField('date found')

	def __str__(self):
		return self.color + " " + self.gem_type

	def get_absolute_url(self):
		return reverse('detail', kwargs={'gem_id': self.id})

class Display(models.Model):
	date_shown = models.DateField('date shown')
	highest_offer = models.IntegerField()
	status = models.CharField(
		max_length=1,
		choices=STATUS_ENUM,
		default=STATUS_ENUM[0][0]
	)
	gem = models.ForeignKey(Gem, on_delete=models.CASCADE)

	def __str__(self): 
		return str(self.date_shown) + " " + self.status

	class Meta:
		ordering = ['-date_shown']