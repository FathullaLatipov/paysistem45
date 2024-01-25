from fastapi import FastAPI

# Подключения в БД
from card.card_api import card_router
from database import Base, engine
from transfers.transfers_api import transaction_router
from user.user_api import user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(card_router)
app.include_router(transaction_router)
app.include_router(user_router)
# Мы первый html с помощью FastAPI 100/100
# Мы сделаем курс валют из NBU 50/50
# Запускаем наш Docker 10/100




