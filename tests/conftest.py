import pytest
from generators import *
from methods.user_methods import UserMethods


# Фикстура, которая генерирует данные для регистрации пользователя и возращает в тест для регистрации
# пользователя. Затем логинится с его email и паролем, получает accessToken и удаляет пользователя после теста
@pytest.fixture
def temporary_user():
    data = generate_user_data()

    yield data

    credentials = {
        "email": data["email"],
        "password": data["password"],
    }
    login_response = UserMethods.login_user(credentials)
    access_token = login_response.json().get("accessToken")

    if access_token:
        UserMethods.delete_user(access_token)


# Фикстура, которая регистрирует пользователя и возвращает его email и пароль для авторизации
@pytest.fixture
def registered_user(temporary_user):
    _, registered_user_data = UserMethods.register_new_user(temporary_user)
    return registered_user_data


# Фикстура, которая авторизует пользователя и возращает access_token
@pytest.fixture
def logged_in_user(registered_user):
    access_token, _ = UserMethods.login_user(registered_user)
    return access_token
