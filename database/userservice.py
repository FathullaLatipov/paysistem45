from database.models import User
from datetime import datetime

from database import get_db


# Регистрация пользователя (name, surname, email, phone, password)
def register_user(name, surname, email, phone_number, password):
    db = next(get_db())
    new_user = User(name=name, surname=surname, email=email,
                    phone_number=phone_number, password=password)
    db.add(new_user)
    db.commit()

    return 'Успешно'


# Получить инфо и пользователе
def get_exact_user_id(user_id):
    db = next(get_db())
    exact_user = db.query(User).filter_by(user_id=user_id).first()

    return exact_user

# Проверка данных через номер телефона
def check_user_phone_db(phone_number):
    db = next(get_db())

    checker = db.query(User).filter_by(phone_number=phone_number).first()

    if checker:
        return checker
    else:
        return 'Нету такого номер телефона'

# Изменить данные у пользователя
def edit_user_db(user_id, edit_type, new_data):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        if edit_type == 'email':
            exact_user.email = new_data
        elif edit_type == 'surname':
            exact_user.surname = new_data

        db.commit()

        return 'Данные успешно изменены'
    else:
        return 'Пользователь не найден'

# Удаление пользователя исходя из id
def delete_user_db(user_id):
    db = next(get_db())

    delete_user = db.query(User).filter_by(user_id=user_id).first()

    if delete_user:
        db.delete(delete_user)
        db.commit()

        return 'Пользователь успешно удален'
    else:
        return 'Пользователь не найден'