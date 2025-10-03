import requests
import allure
from urls import *
from helper import get_credentials


class UserMethods:
    @staticmethod
    @allure.step("Регистрация нового пользователя")
    def register_new_user(data):
        headers = {"Content-Type": "application/json"}
        register_response = requests.post(REGISTER_USER, json=data, headers=headers)
        registered_user_data = None
        response_body = register_response.json()
        if (
            register_response.status_code in [200, 201]
            and response_body.get("success") is True
        ):
            registered_user_data = {
                "email": response_body.get("user", {}).get("email"),
                "password": data["password"],
            }
        return register_response, registered_user_data

    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(data):
        access_token = None
        refresh_token = None

        payload = get_credentials(data)
        login_response = requests.post(LOGIN_USER, json=payload)
        response_body = login_response.json()
        if response_body.get("success") == True:
            access_token = response_body.get("accessToken")
            refresh_token = response_body.get("refreshToken")
        return login_response, access_token, refresh_token

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(access_token):
        headers = {"Authorization": access_token}
        delete_user_response = requests.delete(DELETE_USER, headers=headers)
        return delete_user_response
