from fastapi import APIRouter
from database.userservice import register_user, edit_user_db, delete_user_db, get_exact_user_id, check_user_phone_db

from datetime import datetime

from user import UserRegisterValidator, EditUserValidator

user_router = APIRouter(prefix='/user', tags=['Работа с пользователями'])

# Регистрация
@user_router.post('/register')
async def register_new_user(data: UserRegisterValidator):
    new_user_data = data.model_dump()

    checker = check_user_phone_db(data.phone_number)

    if checker:
        return {'message': 'Пользователь с таким номером уже есть в БД'}
    else:
        result = register_user(reg_date=datetime.now(), **new_user_data)

        return {'message': result}

# Получение информации о пользователе
@user_router.get('/info')
async def get_user(user_id: int):
    result = get_exact_user_id(user_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Такого пользователя нету(('}

# Изменить данные пользователя
@user_router.put('/edit-data')
async def edit_user(data:EditUserValidator):
    change_data = data.model_dump()

    result = edit_user_db(**change_data)

    return {'message': result}

# Удалить пользователя
@user_router.delete('/delete-user')
async def delete_user(user_id: int):
    result = delete_user_db(user_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Такого пользователя нету!((('}