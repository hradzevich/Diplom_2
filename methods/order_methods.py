import requests
import allure
from urls import *


class OrderMethods:
    @staticmethod
    @allure.step("Создание нового заказа")
    def create_new_order(ingredients, access_token=None):
        headers = {"Content-Type": "application/json"}
        if access_token:
            headers["Authorization"] = access_token

        payload = {"ingredients": ingredients}
        create_order_response = requests.post(
            CREATE_ORDER_URL, json=payload, headers=headers
        )
        return create_order_response

    @staticmethod
    @allure.step("Получение данных об ингредиентах")
    def get_ingredients():
        get_ingredients_response = requests.get(GET_INGREDIENTS_URL)
        response_body = get_ingredients_response.json()
        list_of_ingredients = response_body.get("data")
        return list_of_ingredients
