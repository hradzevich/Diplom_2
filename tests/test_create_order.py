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
        "Успешное создание нового заказа с ингредиентами авторизованным пользователем"
    )
    @allure.description(
        "Тест проверяет, что заказ с ингредиентами успешно создан для авторизованного пользователя"
    )
    def test_create_order_by_already_logged_in_user_success(
        self, order_ingredients, user_access_token
    ):
        with allure.step("Создание заказа"):
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

    @allure.title(
        "Ошибка при попытке создания заказа с ингредиентами неавторизованным пользователем"
    )
    @allure.description(
        "Тест проверяет, что при создании заказа без авторизации сервер возвращает ошибку"
    )
    def test_create_order_by_nonauthorized_user_error(self, order_ingredients):
        with allure.step("Создание заказа"):
            create_order_response = OrderMethods.create_new_order(order_ingredients)

        with allure.step("Проверяем статус-код"):
            assert create_order_response.status_code in [
                401,
                403,
            ], f"Ожидался статус 401 или 403, получили {create_order_response.status_code}"

        response_body = create_order_response.json()

        with allure.step("Проверяем тело ответа"):
            assert (
                response_body.get("success") is False
            ), "Флаг 'success' в ответе не равен False"
            assert "name" not in response_body, "В ответе присутствует 'name'"
            assert (
                "order" not in response_body
            ), "В ответе присутствует 'order', хотя пользователь неавторизован"

    @allure.title(
        "Ошибка при попытке создания заказа авторизованным пользователем без ингредиентов"
    )
    @allure.description(
        "Тест проверяет, что заказ не может быть создан успешно без ингредиентов"
    )
    def test_create_order_without_ingredients_error(self, user_access_token):
        with allure.step("Создание заказа"):
            order_ingredients = []
            create_order_response = OrderMethods.create_new_order(
                order_ingredients, user_access_token
            )

        with allure.step("Проверяем статус-код"):
            assert (
                create_order_response.status_code == 400
            ), f"Ожидался статус 400, получили {create_order_response.status_code}"

        response_body = create_order_response.json()

        with allure.step("Проверяем тело ответа"):
            assert (
                response_body.get("success") is False
            ), "Флаг 'success' в ответе не равен False"
            assert (
                response_body["message"] == NO_INGREDIENTS_IN_ORDER_ERROR_MESSAGE
            ), f"Ожидалось сообщение '{NO_INGREDIENTS_IN_ORDER_ERROR_MESSAGE}', получили '{response_body['message']}'"

    @allure.title("Ошибка при попытке создания заказа неверным хешем ингредиента")
    @allure.description(
        "Тест проверяет, что заказ не может быть создан успешно, если передан неверный хеш ингредиента"
    )
    def test_create_order_with_wrong_id_of_ingredient_error(
        self, order_ingredients, user_access_token
    ):
        with allure.step("Создание заказа"):
            order_ingredients_with_invalid_id = modify_ids_of_ingredients(
                order_ingredients
            )
            create_order_response = OrderMethods.create_new_order(
                order_ingredients_with_invalid_id, user_access_token
            )

        with allure.step("Проверяем статус-код"):
            assert (
                create_order_response.status_code == 500
            ), f"Ожидался статус 500, получили {create_order_response.status_code}"
