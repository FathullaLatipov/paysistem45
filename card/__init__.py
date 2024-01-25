from pydantic import BaseModel


# Валидатор для добавлении карты
class AddCardValidator(BaseModel):
    user_id: int
    card_number: int
    balance: float
    card_name: str
    exp_date: int
