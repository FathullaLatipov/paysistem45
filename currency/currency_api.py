from fastapi import APIRouter, Depends
import requests


currency_router = APIRouter(prefix='/currency', tags=['Курсы валют'])


# Проверка редис базы есть ли там информация про курс валют
# def check_currency_rates_redis():
#     usd = redis_db.get("USD")
#     rub = redis_db.get("RUB")
#     eur = redis_db.get("EUR")
#
#     if usd and rub and eur:
#         return {'USD': usd.decode(), 'RUB': rub.decode(), 'EUR': eur.decode()}
#     else:
#         return False


# Запрос на получение всех курсов валют
@currency_router.post('/get-rates')
async def get_currency_rates():
    nbu_url = 'https://nbu.uz/uz/exchange-rates/json/'
    usd = requests.get(nbu_url).json()[-1]
    rub = requests.get(nbu_url).json()[-6]
    eur = requests.get(nbu_url).json()[7]

    # Сохраняем только те валюты которые нам нужны
    return {'USD': usd, 'RUB': rub, 'EUR': eur}
