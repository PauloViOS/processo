from django.db import models


class Stock(models.Model):
	ticker = models.CharField(max_length=10, primary_key=True)
	company_name = models.CharField(max_length=40, null=True)

	def __str__(self):
		return self.ticker


class HistoricalPrice(models.Model):
	stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
	timestamp = models.IntegerField()
	price = models.DecimalField(max_digits=10, decimal_places=2)

	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['stock', 'timestamp'], name='dated_price')
		]
