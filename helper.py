from generators import *
from faker import Faker
import random as r

# Функция в копии словаря original_data заменяет значение указанного ключа на другое.
# Используется для тестирования сценариев с неправильным логином/паролем
def modify_user_data(original_data, key):
    data = original_data.copy()
    if key == "email":
        data[key] = fake.name() + str(r.randint(101, 200))
    elif key == "password":
        data[key] = fake.password(
            length=5,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        )
    return data