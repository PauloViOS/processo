from django.db import models


class Portfolio(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Stock(models.Model):
    ticker = models.CharField(max_length=10, primary_key=True)
    company_name = models.CharField(max_length=40, null=True)
    upper_limit = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    lower_limit = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    portfolio = models.ForeignKey(Portfolio, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.ticker


class HistoricalPrice(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    datetime = models.DateTimeField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["stock", "datetime"], name="dated_price")
        ]
        ordering = ["stock", "-datetime"]
