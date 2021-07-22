from django.db import models

class Dealer(models.Model):
	name = models.CharField(max_length=60)

	def __str__(self):
		return self.name

class Car(models.Model):
	name = models.CharField(max_length=60)
	mark = models.CharField(max_length=60)
	dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE)

	def __str__(self):
		return self.name