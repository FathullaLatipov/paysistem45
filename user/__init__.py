from pydantic import BaseModel


# Валидатор для регистрации
class UserRegisterValidator(BaseModel):
    name: str
    surname: str
    email: str
    phone_number: str
    password: str
    city: str

# Валидатор изменении данных пользователя
class EditUserValidator(BaseModel):
    user_id: int
    edit_type: str
    new_data: str