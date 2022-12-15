from django.shortcuts import render


def home(request):
	return render(request, 'home.html', {})


def all_stocks(request):
	return render(request, 'all_stocks.html', {})