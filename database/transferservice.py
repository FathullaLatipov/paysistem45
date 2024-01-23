from database.models import Transfer, UserCard
from datetime import datetime

from database import get_db


# Проверка карты
def validate_card(card_number, db):
    exact_card = db.query(UserCard).filter_by(card_number=card_number).first()

    return exact_card


# Создание перевода
def create_transaction_db(card_from, card_to, amount):
    db = next(get_db())

    # Проверка на наличии обеих карты в БД
    check_card_from = validate_card(card_from, db)  # 1
    check_card_to = validate_card(card_to, db)  # 2

    # Если обе карты существуют в бд перевод
    if check_card_from and check_card_to:
        # Проверка баланса у отправителя
        if check_card_from.balance >= amount:
            # Минусуем у того кто отправляет
            check_card_from.balance -= amount
            # Добавляем тому кто получает
            check_card_to.balance += amount

            # Cохраняем платеж в бд
            new_transaction = Transfer(card_from_id=check_card_from.card_id,
                                       card_to_id=check_card_to.card_id, amount=amount,
                                       transaction_date=datetime.now()
                                       )
            db.add(new_transaction)
            db.commit()

            return 'Перевод успешно выполнен'
        else:
            return "Недостаточно средств на балансе"
    else:
        return "Одна из карт не существует("

# Получить все переводы по карте(card_id) история
def get_card_transaction_db(card_from_id):
    db = next(get_db())

    card_transaction = db.query(Transfer).filter_by(card_from_id=card_from_id).all()
    return card_transaction

# ДЗ ОТменить перевод подсказка как бы create_transaction_db но немного по другому и там будет
# статус как False Я спрошу у каждого!
# def cancel_transfer_db(card_from, card_to, amount, transfer_id)