from django.shortcuts import render
import requests
import json


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
	api_request = requests.get("https://brapi.dev/api/quote/PETR4")

	try:
		stock = json.loads(api_request.content)["results"][0]
	except Exception as e:
		api = "Erro..."

	return render(request, 'stock.html', {'stock':stock})