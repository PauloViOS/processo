from django.shortcuts import render
import requests
import json


def home(request):
	return render(request, 'home.html', {})


def all_stocks(request):
	api_request = requests.get("https://brapi.dev/api/quote/list")

	try:
		api = json.loads(api_request.content)["stocks"]
	except Exception as e:
		api = "Erro..."

	return render(request, 'all_stocks.html', {'api':api})