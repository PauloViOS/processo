from django.contrib import admin
from .models import Stock, HistoricalPrice


class StockAdmin(admin.ModelAdmin):
	list_display = ('ticker', 'company_name')

class HistoricalPriceAdmin(admin.ModelAdmin):
	list_display = ('stock', 'timestamp', 'price')

admin.site.register(Stock, StockAdmin),
admin.site.register(HistoricalPrice, HistoricalPriceAdmin)
