from dataclasses import dataclass

# Создаем дата класс для имитации нового пользователя с валидными данными при регестрации
# потом используем это в generator.py
@dataclass
class Person_with_valid_data:
    email:str = None
    password:str = None
    user_name:str = None
