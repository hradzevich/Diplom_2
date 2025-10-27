# Здесь собраны API-ручки для автотестов сервиса Stellar Burgers

BASE_URL = "https://stellarburgers.nomoreparties.site"

# Регистрация пользователя
REGISTER_USER_URL = f"{BASE_URL}/api/auth/register"

# Авторизация пользователя
LOGIN_USER_URL = f"{BASE_URL}/api/auth/login"

# Удаление пользователя
DELETE_USER_URL = f"{BASE_URL}/api/auth/user"

# Создание заказа
CREATE_ORDER_URL = f"{BASE_URL}/api/orders"

# Получение  данных об ингредиентах
GET_INGREDIENTS_URL = f"{BASE_URL}/api/ingredients"