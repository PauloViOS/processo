from .models import Stock, HistoricalPrice
from datetime import datetime
import requests
import json
from django.conf import settings
from django.core.mail import send_mail

def populate_db_with_stock_names(all_stocks):
	for stock in all_stocks:
		stock_symbol = stock["stock"]
		instance = Stock(ticker=stock_symbol)
		instance.save()

	return "Foi"

def get_all_stock_names_in_single_string():
	stocks = Stock.objects.all()
	names = ''
	for stock in stocks:
		names += f'{stock.ticker},'
	names = names[:-1]
	return names


def populate_db_with_stock_company_names():
	names = get_all_stock_names_in_single_string()
	api_request = requests.get(f"https://brapi.dev/api/quote/{names}?range=3mo&interval=1d")
	all_stocks = json.loads(api_request.content)["results"]
	for stock in all_stocks:
		ticker=stock["symbol"]
		instance = Stock.objects.get(ticker=ticker)
		instance.company_name = stock["longName"] if "longName" in stock.keys() else None
		instance.save()


def convert_unix_to_dt(unixtime):
	dt = datetime.fromtimestamp(unixtime)
	return dt


def get_1mo_historical_prices():
	names = Stock.objects.all()
	for name in names:
		api_request = requests.get(f"https://brapi.dev/api/quote/{name}?range=1mo&interval=1d")
		stock_info  = json.loads(api_request.content)
		if "error" in stock_info.keys():
			continue
		stock_info = stock_info["results"][0]
		if "historicalDataPrice" not in stock_info.keys():
			continue
		stock_instance=Stock.objects.get(ticker=stock_info["symbol"])
		for historical_price in stock_info["historicalDataPrice"]:
			unixtime = historical_price["date"]
			price = historical_price["close"]
			dt_timestamp = convert_unix_to_dt(unixtime)
			instance = HistoricalPrice(stock=stock_instance, datetime=dt_timestamp, price=price)
			instance.save()


def test_email():
	subject = "Chupa"
	message = "Mandei usando django. Facinho po"
	email_from = settings.EMAIL_HOST_USER
	recipient_list = ['arthurpdesimone@gmail.com', 'pv8592@gmail.com']
	send_mail(subject, message, email_from, recipient_list)
	return "foi hein"
