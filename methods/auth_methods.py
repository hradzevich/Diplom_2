import requests
import allure
from urls import *


class UserMethods:
    @staticmethod
    @allure.step("Регистрация нового пользователя")
    def register_new_user(data):
        register_response = requests.post(REGISTER_USER, json=data)
        registered_user_data = None
        if register_response.json().get("success") == True:
            registered_user_data = {
                "email": register_response.json().get("user", {}).get("email"),
                "password": data["password"],
            }
        return register_response, registered_user_data

    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(data):
        login_response = requests.post(REGISTER_USER, json=data)
        if login_response.json().get("success") == True:
            access_token = login_response.json().get("accessToken")
            refresh_token = login_response.json().get("refreshToken")
        return login_response, access_token, refresh_token

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(access_token):
        headers = {"Authorization": access_token}
        delete_user_response = requests.delete(DELETE_USER, headers=headers)
        return delete_user_response
