from generators import *
from faker import Faker
import random as r
import string as s

fake = Faker()


# Разбивает список ингредиентов на категории и формирует ingredients для payload
# для создания заказа с 1 булкой, 1 начинкой и 1 соусом
def create_order_with_ingredients_payload(list_of_ingredients):
    buns, mains, sauces = [], [], []
    for ingr in list_of_ingredients:
        if ingr["type"] == "bun":
            buns.append(ingr["_id"])
        if ingr["type"] == "main":
            mains.append(ingr["_id"])
        if ingr["type"] == "sauce":
            sauces.append(ingr["_id"])

    order_ingredients = []
    if buns:
        order_ingredients.append(buns[0])
    if mains:
        order_ingredients.append(mains[0])
    if sauces:
        order_ingredients.append(sauces[0])

    return order_ingredients


# Функция формирует словарь с данными для авторизации пользователя
def get_credentials(data):
    return {"email": data["email"], "password": data["password"]}


# Функция в копии словаря original_data заменяет значение указанного ключа на другое.
# Используется для тестирования сценариев с неправильным логином/паролем
def modify_user_data(original_data, key):
    data = original_data.copy()
    if key == "email":
        data[key] = fake.email()
    elif key == "password":
        data[key] = fake.password(
            length=5,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        )
    return data


# Возвращает копию списка ingredient_id с невалидным ID для тесто
def modify_ids_of_ingredients(original_data):
    data = list(original_data)
    data[0] = "".join(r.choices(s.ascii_letters + s.digits, k=24))
    return data


# Удаляет из копии словаря original_data поле с именем key.
# Используется для тестирования негативных сценариев
def prepare_data_without_field(original_data, key):
    data = original_data.copy()
    data.pop(key, None)
    return data
