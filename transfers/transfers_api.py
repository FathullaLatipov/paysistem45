from fastapi import APIRouter

from database.transferservice import create_transaction_db, get_card_transaction_db, cancel_transfer_db

from transfers import CreateTransactionValidator, CancelValidator

transaction_router = APIRouter(prefix='/transaction', tags=['Работа с платежами'])


# Запрос на создание транзакции
@transaction_router.post('/create')
async def add_new_transaction(data: CreateTransactionValidator):
    transaction_data = data.model_dump()
    result = create_transaction_db(**transaction_data)

    if result:
        return {'message': result}
    else:
        return {'message': 'Ошибка короче!'}


# Получить все переводы по карте
@transaction_router.get('/get-transactions')
async def get_transactions(card_id: int):
    result = get_card_transaction_db(card_from_id=card_id)
    if result:
        return result
    else:
        return {'message': 'Короче ошибка!'}


# Отмена транзкации
@transaction_router.post('/cancel-transaction')
async def cancel_transaction(data: CancelValidator):
    cancel_data = data.model_dump()
    result = cancel_transfer_db(**cancel_data)

    if result:
        return {'message': result}
    else:
        return {'message': 'Ошибка короче!'}
