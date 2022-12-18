from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
import requests
import json
from django.http import HttpResponse

from .models import Stock, HistoricalPrice, Portfolio
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


def stock(request, ticker=None):
	if ticker:
		stock_instance = get_object_or_404(Stock, ticker=ticker)
		historical_price = HistoricalPrice.objects.filter(stock=stock_instance).last()
		price = historical_price.price

		return render(request, 'stock.html', {'stock':stock_instance, 'price':price})
	else:
		return render(request, 'stock.html', {})


def portfolio(request):
	portfolio_stocks = Stock.objects.filter(portfolio__id=1)
	if not portfolio_stocks:
		return render(request, 'portfolio.html', {})
	return render(request, 'portfolio.html', {"portfolio_stocks":portfolio_stocks})

def add_stock(request, ticker):
	stock = Stock.objects.get(ticker=ticker)
	pf = Portfolio.objects.get(pk=1)
	stock.portfolio = pf
	stock.save()
	return redirect('/')


def remove_stock(request, ticker):
	stock = Stock.objects.get(ticker=ticker)
	pf = Portfolio.objects.get(pk=1)
	stock.portfolio = None
	stock.save()
	return redirect('/portfolio')


def sign_up(request):
	return render(request, 'sign_up.html', {})