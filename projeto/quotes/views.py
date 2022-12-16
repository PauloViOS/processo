from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import json

from .models import Stock
from .forms import StockForm

def home(request):
	return render(request, 'home.html', {})


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
		api_request = requests.get(f"https://brapi.dev/api/quote/{stock_symbol}")
		try:
			stock_info = json.loads(api_request.content)["results"][0]
		except Exception as e:
			stock_info = "Erro..."
		return render(request, 'stock.html', {'stock':stock_info})
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