from database.models import UserCard
from datetime import datetime

from database import get_db

# Добавлять карту
def add_card_db(user_id, card_number, balance, card_name, exp_date):
    db = next(get_db())

    new_card = UserCard(user_id=user_id, card_number=card_number, balance=balance,
                        card_name=card_name, exp_date=exp_date)

    db.add(new_card)
    db.commit()

    return 'Карта успешно добавлено'

# Вывести все карты определенного пользователя
def get_exact_user_card_db(user_id):
    db = next(get_db)

    exact_user_card = db.query(UserCard).filter_by(user_id=user_id).first()

    return exact_user_card

# Проверка карты на наличия в БД
def check_card_db(card_number):
    db = next(get_db)

    checker = db.query(UserCard).filter_by(card_number=card_number).first()

    if checker:
        return checker
    else:
        return 'Такого карты нету(('

# Удаления карты
def delete_card_db(card_id):
    db = next(get_db())

    delete_card = db.query(UserCard).filter_by(card_id=card_id).first()

    if delete_card:
        db.delete(delete_card)
        db.commit()

        return 'Карта успешно удалена'
    else:
        return 'Карта не найдено((('