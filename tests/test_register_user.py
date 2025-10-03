import pytest
import allure
from methods.user_methods import UserMethods
from generators import *
from data import *
from helper import *


@allure.parent_suite("API тесты Stellar Burger")
@allure.suite("Пользователь")
@allure.sub_suite("Создание пользователя")
class TestRegisterUser:
    @allure.title("Успешная регистрация нового пользователя")
    @allure.description(
        "Тест проверяет успешную регистрацию нового пользователя через API Stellar Burgers"
    )
    def test_register_new_user(self, temporary_user):
        with allure.step("Регистрация нового пользователя"):
            register_response, _ = UserMethods.register_new_user(temporary_user)

        with allure.step("Проверяем статус-код"):
            assert register_response.status_code in [
                200,
                201,
            ], f"Ожидался статус 200 или 201, получили {register_response.status_code}"

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

    @allure.title("Регистрация пользователя, который уже существует")
    @allure.description(
        "Тест проверяет, что при попытке зарегистрировать пользователя "
        "с данными, которые уже есть в системе, API возвращает статус-код 403 и сообщение об ошибке"
    )
    def test_register_existing_user_returns_error(
        self, registered_user, temporary_user
    ):
        with allure.step("Получение email ранее зарегистрированного пользователя"):
            existing_user_email = registered_user["email"]

        with allure.step("Подготовка данных для повторной регистрации с тем же email"):
            new_user_data = {
                "email": existing_user_email,
                "password": temporary_user["password"],
                "name": temporary_user["name"],
            }

        with allure.step("Регистрация нового пользователя с уже используемым email"):
            register_response, _ = UserMethods.register_new_user(new_user_data)

        with allure.step("Проверяем статус-код"):
            assert (
                register_response.status_code == 403
            ), f"Ожидался статус 403, получили {register_response.status_code}"

        response_body = register_response.json()

        with allure.step("Проверяем тело ответа"):
            assert (
                response_body.get("success") is False
            ), "Флаг 'success' в ответе не равен False"
            assert "message" in response_body, "В ответе отсутствует ключ 'message'"
            assert (
                response_body.get("message") == REGISTER_EXISRING_USER_ERROR_MESSAGE
            ), f"Сообщение в ответе '{response_body.get("message")}' не совпадает с ожидаемым '{REGISTER_EXISRING_USER_ERROR_MESSAGE}'"

    @allure.title(
        "Ошибка при регистрации пользователя с отсутствующим обязательным полем"
    )
    @allure.description(
        "Тест проверяет, что при попытке зарегистрировать пользователя без обязательного поля "
        "(email, password, name) API возвращает код 403 и корректное сообщение об ошибке"
    )
    @pytest.mark.parametrize("key", ["email", "password", "name"])
    def test_register_new_user_without_requered_field_returns_error(
        self, key, temporary_user
    ):
        with allure.step(f"Регистрация нового пользователя без {key}"):
            data_with_empty_required = prepare_data_without_field(temporary_user, key)
            register_response, _ = UserMethods.register_new_user(
                data_with_empty_required
            )
        with allure.step("Проверяем код ответа"):
            assert (
                register_response.status_code == 403
            ), f"Ожидали статус-код 403, получили {register_response.status_code}"

        response_body = register_response.json()

        with allure.step("Проверяем тело ответа"):
            assert (
                response_body.get("success") is False
            ), "Флаг 'success' в ответе не равен False"
            assert "message" in response_body, "В ответе отсутствует ключ 'message'"
            assert (
                response_body.get("message")
                == REGISTER_USER_WITH_NO_REQUIRED_FIELD_ERROR_MESSAGE
            ), f"Сообщение в ответе '{response_body.get("message")}' не совпадает с ожидаемым '{REGISTER_USER_WITH_NO_REQUIRED_FIELD_ERROR_MESSAGE}'"
