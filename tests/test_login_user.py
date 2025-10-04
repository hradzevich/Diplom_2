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
            credentials = get_credentials(registered_user)
            login_response = UserMethods.login_user(credentials)

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

    @allure.title("Ошибка при логине пользователя с неверным email или паролем")
    @allure.description(
        "Тест проверяет, что при попытке логина с неверным email или password "
        "API возвращает код 401 и корректное сообщение об ошибке."
    )
    @pytest.mark.parametrize("key", ["email", "password"])
    def test_login_user_with_wrong_login_or_password_error(self, key, registered_user):
        with allure.step(f"Логин пользователя c неправильным {key}"):
            credentials = get_credentials(registered_user)
            invalid_credentials = modify_user_data(credentials, key)
            login_response = UserMethods.login_user(invalid_credentials)

        with allure.step("Проверяем статус-код"):
            assert (
                login_response.status_code == 401
            ), f"Ожидался статус 401, получили {login_response.status_code}"

        response_body = login_response.json()

        with allure.step("Проверяем тело ответа"):
            assert (
                response_body.get("success") is False
            ), "Флаг 'success' в ответе не равен False"
            assert "message" in response_body, "В ответе отсутствует ключ 'message'"
            assert (
                response_body.get("message")
                == LOGIN_WITH_WRONG_CREDENTIALS_ERROR_MESSAGE
            ), f"Сообщение в ответе '{response_body.get("message")}' не совпадает с ожидаемым '{LOGIN_WITH_WRONG_CREDENTIALS_ERROR_MESSAGE}'"
