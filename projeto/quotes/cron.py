import json
from datetime import datetime

import requests
from stocks_svc import get_all_stock_names_in_single_string

from .models import HistoricalPrice, Stock


def get_stock_prices_every_minute():
    names = get_all_stock_names_in_single_string()
    api_request = requests.get(f"https://brapi.dev/api/quote/{names}")
    all_stocks = json.loads(api_request.content)["results"]
    now = datetime.now().replace(second=0, microsecond=0)
    for stock in all_stocks:
        if "error" in stock.keys():
            continue
        ticker = stock["symbol"]
        stock_instance = Stock.objects.get(ticker=ticker)
        price = stock["regularMarketPrice"]
        instance = HistoricalPrice(stock=stock_instance, datetime=now, price=price)
        instance.save()
