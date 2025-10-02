import pytest
import allure
from methods.user_methods import UserMethods
from generators import *


@allure.parent_suite("API тесты Stellar Burger")
@allure.suite("Пользователь")
@allure.sub_suite("Создание пользователя")
class TestRegisterUser:
    @allure.title("Успешная регистрация нового пользователя")
    @allure.description("")
    def test_register_new_user(self, temporary_user):
        with allure.step("Регистрация нового пользователя"):
            register_response, _ = UserMethods.register_new_user(temporary_user)

        with allure.step("Проверяем статус-код"):
            assert (
                register_response.status_code == 201
                or register_response.status_code == 200
            ), f"Ожидался статус 200 или 201, получили {register_response.status_code}"

        response_body = register_response.json()

        with allure.step("Проверяем тело ответа"):
            assert (
                response_body.get("success") is True
            ), "Флаг 'success' в ответе не равен True"
            assert "user" in response_body, "В ответе отсутствует ключ 'user'"
            assert (
                response_body["user"].get("email") == temporary_user["email"]
            ), f"Email в ответе {response_body['user'].get('email')} не совпадает с ожидаемым {temporary_user['email']}"
            assert (
                response_body["user"].get("name") == temporary_user["name"]
            ), f"Имя в ответе {response_body['user'].get('name')} не совпадает с ожидаемым {temporary_user['name']}"
            assert "accessToken" in response_body, "В ответе отсутствует 'accessToken'"
            assert (
                "refreshToken" in response_body
            ), "В ответе отсутствует 'refreshToken'"
