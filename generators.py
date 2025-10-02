from faker import Faker
import random as r

fake = Faker()


# Генерирует необходимые для создания пользователя данные
def generate_user_data():

    name = fake.user_name()
    password = fake.password(
        length=7,
        special_chars=True,
        digits=True,
        upper_case=True,
        lower_case=True,
    )
    email = fake.email()

    return {
        "email": email,
        "password": password,
        "name": name,
    }
