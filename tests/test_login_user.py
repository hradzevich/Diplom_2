import pytest
import allure
from methods.user_methods import UserMethods
from data import *
from helper import *


@allure.parent_suite("API тесты Stellar Burger")
@allure.suite("Пользователь")
@allure.sub_suite("Авторизация пользователя")
class TestLoginUser:
    @allure.title("Успешная авторизация существующего пользователя")
    @allure.description(
        "Тест проверяет, что после регистрации пользователя можно успешно выполнить логин "
        "с передачей всех обязательных полей (email, password)"
    )
    def test_login_existing_user_success(self, registered_user):
        with allure.step("Логин пользователя"):
            credentials = {
                "email": registered_user["email"],
                "password": registered_user["password"],
            }
            login_response, _, _ = UserMethods.login_user(credentials)

        with allure.step("Проверяем статус-код"):
            assert login_response.status_code in [
                200,
                201,
            ], f"Ожидался статус 200 или 201, получили {login_response.status_code}"

        response_body = login_response.json()

        with allure.step("Проверяем тело ответа"):
            assert (
                response_body.get("success") is True
            ), "Флаг 'success' в ответе не равен True"
            assert "accessToken" in response_body, "В ответе отсутствует 'accessToken'"
            assert (
                "refreshToken" in response_body
            ), "В ответе отсутствует 'refreshToken'"
            assert "user" in response_body, "В ответе отсутствует ключ 'user'"
            assert (
                response_body["user"].get("email") == registered_user["email"]
            ), f"Email в ответе {response_body['user'].get('email')} не совпадает с ожидаемым {registered_user['email']}"
            assert (
                response_body["user"].get("name") == registered_user["name"]
            ), f"Имя в ответе {response_body['user'].get('name')} не совпадает с ожидаемым {registered_user['name']}"
