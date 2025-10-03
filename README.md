# Дипломный проект. Задание 2: Автотесты для API

### Студент: Родевич Анна

### <h>Когорта: FS-28</h>
<hr>

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

## Реализованные сценарии

### Создание пользователя:
`test_register_new_user_success` – регистрация нового пользователя с уникальными данными
`test_register_existing_user_error` – проверка ошибки при попытке регистрации уже существующего пользователя
`test_register_new_user_without_requered_field_error` – проверка, что при отсутствии email, password или name регистрация не проходит

### Логин пользователя:
```test_login_existing_user_success``` – проверка успешного логина под существующим пользователем
```test_login_user_with_wrong_login_or_password_error``` проверка, что при неверном email или password возвращается ошибка

### Создание заказа:
`test_create_order_already_logged_in_user_success` – успешное создание заказа авторизованным пользователем
`test_create_order_by_nonauthorized_user_error` – проверка, что заказ без авторизации не создается
`test_create_order_without_ingredients_error` – проверка, что заказ не может быть создан успешно без ингредиентов
`test_create_order_with_wrong_id_of_ingredient_error` – проверка, что при передаче неверного ingredient_id сервер возвращает ошибку


## Структура проекта

- `methods` - пакет, содержащий методы работы с API
- `tests` - пакет с тестами, разделёнными по функционалу
- `data.py` - файл с текстовыми данными
- `generators.py` - файл с функциями генерации данных для тестов
- `helper.py` - файл с вспомогательными функциями для подготовки payload, модификации данных, работы с ингредиентами
- `requirements.txt` - файл с зависимостями проекта 
- `urls.py` - файл с базовыми URL эндпоинтов API

### Технологии
+ Python 3.13.5

+ Pytest

+ Faker (для генерации тестовых данных)

+ Random (для модификации тестовых данных)

+ Allure (отчёты о тестировании)


### Запуск тестов

1. Клонировать репозиторий:<br/>
    ```git clone git@github.com:hradzevich/Diplom_2.git  ```

2. Установить зависимости:<br/>
    ```pip install -r requirements.txt```

3. Запустить тесты с сохранением результатов для Allure:<br/>
    ```pytest --alluredir=allure-results```

4. Сгенерировать html-отчёт в папку allure_report:<br/>
    ```allure generate allure-results -o allure_report --clean```

5. Открыть готовый отчёт в браузере:<br/>
    ```allure open allure_report```


### Полезные команды 

Очистить результаты прошлых запусков:<br/>
    ```rm -rf allure-results allure_report```

Перегенерировать отчёт без запуска тестов (если тесты уже запускались и в папке allure_results есть данные):<br/>
    ```allure generate allure-results -o allure_report --clean```
    ```allure open allure_report```

Быстрый просмотр отчёта без сохранения (отчёт откроется во временном режиме, готовая папка не создаётся):<br/>
    ```allure serve allure-results```