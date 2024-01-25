from fastapi import APIRouter

from card import AddCardValidator
from database.cardservice import check_card_db, add_card_db, get_exact_user_card_db, get_exact_user_cards_db, delete_card_db

card_router = APIRouter(prefix='/card', tags=['Работа с картами'])

# Добавления карты add_new_card
@card_router.post('/add')
async def add_new_card(data: AddCardValidator):
    card_data = data.model_dump()

    # Проверка карты на наличие в БД
    checker = check_card_db(data.card_number)

    if checker:
        return {'Message': 'Карта с такми номером есть в базе'}
    else:
        result = add_card_db(**card_data)
        return {'message': result}

# Получить инфо определенного пользователя определнного карты  get_card_info
@card_router.get('/exact-cards-info')
async def get_user_card_info(card_id: int, user_id: int):
    result = get_exact_user_cards_db(user_id=user_id, card_id=card_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Карта не найдена(('}

# Запрос на получении всех карт определенного пользователя
@card_router.get('/exact-card-info')
async def get_user_cards_info(user_id: int):
    result = get_exact_user_card_db(user_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Такого пользователя нету(('}

# Запрос на удаления карты
@card_router.delete('/delete-card')
async def delete_card(card_id: int):
    result = delete_card_db(card_id)

    if result:
        return {'message': f'Success {result}'}
    else:
        return {'message': 'Нету такого карты('}