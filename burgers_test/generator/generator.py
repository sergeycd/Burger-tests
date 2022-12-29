# импортируем dataclass из data.py
from Data.data import Person_with_valid_data

# импортируем библиотеку для генерации фэйковых данных
from faker import Faker

# импортируем рандом что бы создавать пароли и прочие данные разной длинны
from random import randint

faker_ru = Faker('ru_RU')


# создаем пользователя с валидными данными
# сначала создаем функцию/метод
def generate_person_with_valid_data():
    # в него добавляем класс из dataclass, предварительно импортировав
    yield Person_with_valid_data(
        # берем данные класса и добавляем им значения с помощью фэйкера
        email=faker_ru.email(),
        password=faker_ru.password(length=randint(6, 12)),
        user_name=faker_ru.name()
    )
    # создаем пользователя с валидными данными
    # сначала создаем функцию/метод


def generate_person_with_failing_password():
    # в него добавляем класс из dataclass, предварительно импортировав
    yield Person_with_valid_data(
        # берем данные класса и добавляем им значения с помощью фэйкера
        email=faker_ru.email(),
        password = faker_ru.password(length=randint(3, 5)),
        user_name=faker_ru.name()
    )

def generate_person_without_name():
    # в него добавляем класс из dataclass, предварительно импортировав
    yield Person_with_valid_data(
        # берем данные класса и добавляем им значения с помощью фэйкера
        email=faker_ru.email(),
        password = faker_ru.password(length=randint(3, 5)),
    )



# (1)создали класс постоянного пользователя и наполнили его в conftest
class UserSite():
        def __init__(self,name,login,password):
            self.name = name
            self.login = login
            self.password = password