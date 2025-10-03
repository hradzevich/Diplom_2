import pytest
import allure
from methods.order_methods import OrderMethods
from data import *
from helper import *


@allure.parent_suite("API тесты Stellar Burger")
@allure.suite("Заказы")
@allure.sub_suite("Создание заказа")
class TestCreateOrder:
    @allure.title(
        "Успешное создание нового заказа авторизованным до создания заказа пользователем"
    )
    @allure.description(
        "Создание заказа авторизованным до оформления заказа пользователем: проверка статуса и структуры ответа"
    )
    def test_create_order_already_logged_in_user_success(
        self, ingredients_data, user_access_token
    ):
        with allure.step("Создание заказа"):
            _, order_ingredients = ingredients_data
            create_order_response = OrderMethods.create_new_order(
                order_ingredients, user_access_token
            )

        with allure.step("Проверяем статус-код"):
            assert create_order_response.status_code in [
                200,
                201,
            ], f"Ожидался статус 200 или 201, получили {create_order_response.status_code}"

        response_body = create_order_response.json()

        with allure.step("Проверяем тело ответа"):
            assert (
                response_body.get("success") is True
            ), "Флаг 'success' в ответе не равен True"
            assert "name" in response_body, "В ответе отсутствует 'name'"
            assert "order" in response_body, "В ответе отсутствует 'order'"
            assert isinstance(
                response_body["order"].get("number"), int
            ), "В ответе номер заказа не число"
