from pydantic import BaseModel


# Валидатор для создании перевода
class CreateTransactionValidator(BaseModel):
    card_from: int
    card_to: int
    amount: float


# Валидатор для отвемы перевода
class CancelValidator(BaseModel):
    card_from: int
    card_to: int
    amount: float
    transfer_id: int
