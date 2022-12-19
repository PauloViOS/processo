from django.contrib import admin

from .models import HistoricalPrice, Portfolio, Stock


class StockAdmin(admin.ModelAdmin):
    list_display = ("ticker", "company_name", "portfolio")


class HistoricalPriceAdmin(admin.ModelAdmin):
    list_display = ("stock", "datetime", "price")


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Stock, StockAdmin),
admin.site.register(HistoricalPrice, HistoricalPriceAdmin)
admin.site.register(Portfolio, PortfolioAdmin),
