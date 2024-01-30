from fastapi import FastAPI

# Для html
from starlette.templating import Jinja2Templates
# Подключения в БД
from card.card_api import card_router
from currency.currency_api import currency_router
from database import Base, engine
from transfers.transfers_api import transaction_router
from user.user_api import user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

# Если хотите выводить html странички
template = Jinja2Templates(directory='templates')

from html_example.html_show import html_router

app.include_router(html_router)

app.include_router(card_router)
app.include_router(transaction_router)
app.include_router(user_router)
app.include_router(currency_router)
# Мы первый html с помощью FastAPI 100/100
# Мы сделаем курс валют из NBU 50/50
# Запускаем наш Docker 100/100
