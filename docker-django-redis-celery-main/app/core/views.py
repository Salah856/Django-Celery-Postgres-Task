from django.shortcuts import render
from .models import ExchangeRate
import requests
import os
from app.app.settings import API_KEY



def postExchangeRate():
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey=' + API_KEY
    res = requests.get(url)
    data = res.json()
    exchange_rate_data = data['Realtime Currency Exchange Rate']
    from_currency_name = exchange_rate_data['2. From_Currency Name']
    to_currency_name = exchange_rate_data['4. To_Currency Name']
    exchange_rate = exchange_rate_data['5. Exchange Rate']
    rate = ExchangeRate(
        from_currency_name=from_currency_name,
        to_currency_name=to_currency_name,
        exchange_rate=exchange_rate)

    rate.save()

    return exchange_rate_data


def getPrices():
    url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&interval=60min&market=CNY&apikey=' + API_KEY
    res = requests.get(url)
    data = res.json()
    return data


def alphaVantageAPI(request):
    if request.method == 'POST':
        postExchangeRate()

    elif request.method == 'GET':
        getPrices()
