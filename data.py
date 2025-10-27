# Cодержит константы с текстовыми сообщениями, которые возвращает
# API при различных сценариях работы


# Текст сообщения при попытке зарегистрировать пользователя с существующим email
REGISTER_EXISRING_USER_ERROR_MESSAGE = "User already exists"

# Текст сообщения при попытке зарегистрировать пользователя без передачи обязательного поля
REGISTER_USER_WITH_NO_REQUIRED_FIELD_ERROR_MESSAGE = (
    "Email, password and name are required fields"
)

# Текст сообщения при попытке авторизации без email или пароля
LOGIN_WITH_WRONG_CREDENTIALS_ERROR_MESSAGE = "email or password are incorrect"

# Текст сообщения при попытке создать заказ без ингредиентов
NO_INGREDIENTS_IN_ORDER_ERROR_MESSAGE = "Ingredient ids must be provided"
