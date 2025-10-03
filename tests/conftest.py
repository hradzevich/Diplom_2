import pytest
from generators import *
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods
from helper import *


# Фикстура, которая генерирует данные для регистрации пользователя и возращает в тест для регистрации
# пользователя. Затем логинится с его email и паролем, получает accessToken и удаляет пользователя после теста
@pytest.fixture
def temporary_user():
    data = generate_user_data()

    yield data

    credentials = get_credentials(data)
    _, access_token, _ = UserMethods.login_user(credentials)

    if access_token:
        UserMethods.delete_user(access_token)


# Фикстура, которая регистрирует пользователя и возвращает его email и пароль для авторизации
@pytest.fixture
def registered_user(temporary_user):
    UserMethods.register_new_user(temporary_user)
    return temporary_user


# Фикстура, которая авторизует пользователя и возращает access_token
@pytest.fixture
def user_access_token(registered_user):
    _, access_token, _ = UserMethods.login_user(registered_user)
    return access_token


# Фикстура, которая получает данные об ингредиентах, формирует и
# возвращает тело запроса для создания заказа и список всех ингредиетов
@pytest.fixture
def order_ingredients():
    ingredients = OrderMethods.get_ingredients()
    return  create_order_with_ingredients_payload(ingredients)
