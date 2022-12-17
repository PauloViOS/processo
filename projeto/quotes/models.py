from django.db import models


class Stock(models.Model):
	ticker = models.CharField(max_length=10, primary_key=True)

	def __str__(self):
		return self.ticker


class HistoricalPrices(models.Model):
	stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
	timestamp = models.IntegerField()
	price = models.DecimalField(max_digits=10, decimal_places=2)
