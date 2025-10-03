from generators import *
from faker import Faker


fake = Faker()

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


# Удаляет из копии словаря original_data поле с именем key.
# Используется для тестирования негативных сценариев
def prepare_data_without_field(original_data, key):
    data = original_data.copy()
    data.pop(key, None)
    return data
