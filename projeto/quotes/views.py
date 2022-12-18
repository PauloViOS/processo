from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import requests
import json

from .models import Stock, HistoricalPrice
from .forms import StockForm


def home(request):
	all_stocks = Stock.objects.all()
	for stock in all_stocks:
		historical_prices = HistoricalPrice.objects.filter(stock=stock)
		prices = []
		for historical_price in historical_prices:
			dateprice = {
				'date': historical_price.datetime,
				'price': historical_price.price
			}
			prices.append(dateprice)
		stock.hist = prices

	return render(request, 'home.html', {'all_stocks':all_stocks})


def all_stocks(request):
	api_request = requests.get("https://brapi.dev/api/quote/list")

	try:
		all_stocks = json.loads(api_request.content)["stocks"]
	except Exception as e:
		api = "Erro..."

	return render(request, 'all_stocks.html', {'all_stocks':all_stocks})


def stock(request):
	if request.method == "POST":
		stock_symbol = request.POST["stock_symbol"]
		stock_instance = get_object_or_404(Stock, ticker=stock_symbol)
		historical_price = HistoricalPrice.objects.filter(stock=stock_instance).last()
		price = historical_price.price

		return render(request, 'stock.html', {'stock':stock_instance, 'price':price})
	else:
		return render(request, 'stock.html', {'stock_symbol': "coloca uma ação ai"})


def add_stock(request):
	if request.method == "POST":
		form = StockForm(request.POST or None)

		if form.is_valid():
			form.save()
			messages.success(request, "Ação foi adicionada ao portfólio")
			return redirect('add_stock')

	else:
		available_stocks = Stock.objects.all()
		return render(request, "add_stock.html", {'available_stocks':available_stocks})


def remove_stock(request, stock_id):
	item = Stock.objects.get(pk=stock_id)
	item.delete()
	messages.success(request, "Ação foi removida do portfólio")
	return redirect('add_stock')
