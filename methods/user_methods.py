import requests
import allure
from urls import *
from helper import get_credentials


class UserMethods:
    @staticmethod
    @allure.step("Регистрация нового пользователя")
    def register_new_user(data):
        headers = {"Content-Type": "application/json"}
        register_response = requests.post(REGISTER_USER_URL, json=data, headers=headers)
        return register_response

    @staticmethod
    @allure.step("Авторизация пользователя")
    def login_user(data):
        headers = {"Content-Type": "application/json"}
        payload = get_credentials(data)
        login_response = requests.post(LOGIN_USER_URL, json=payload, headers=headers)
        return login_response

    @staticmethod
    @allure.step("Удаление пользователя")
    def delete_user(access_token):
        headers = {"Authorization": access_token}
        delete_user_response = requests.delete(DELETE_USER_URL, headers=headers)
        return delete_user_response
