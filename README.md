# API для Yatube

[![Python](https://img.shields.io/badge/-Python-464641?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-464646?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![Pytest](https://img.shields.io/badge/Pytest-464646?style=flat-square&logo=pytest)](https://docs.pytest.org/en/6.2.x/)
[![Postman](https://img.shields.io/badge/Postman-464646?style=flat-square&logo=postman)](https://www.postman.com/)

# Описание

Яндекс Практикум. Спринт 14. Проект спринта: API для Yatube.

# Функционал

- Подписка и отписка от авторизованного пользователя
- Авторизованный пользователь просматривает посты, создает новые, удаляет и изменяет их
- Просмотр сообществ
- Комментирование, просмотр, удаление и обновление комментариев
- Фильтрация по полям.

# Установка

1. Клонировать репозиторий:

    ```sh
    git clone https://github.com/Raul2455/api_final_yatube-master.git
    ```

2. Перейти в папку с проектом:

    ```sh
    cd api_final_yatube/
    ```

3. Установить виртуальное окружение для проекта:

    ```sh
    python -m venv venv
    ```

4. Активировать виртуальное окружение для проекта:

    ```sh
    # для OS Linux и MacOS
    source venv/bin/activate

    # для OS Windows
    source venv/Scripts/activate
    ```

5. Установить зависимости:

    ```sh
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

6. Выполнить миграции на уровне проекта:

    ```sh
    cd yatube
    python manage.py makemigrations
    python manage.py migrate
    ```

7. Запустить проект:

    ```sh
    python manage.py runserver
    ```

# Примеры запросов

Получение токена

Отправить POST-запрос на адрес `api/v1/jwt/create/` и передать 2 поля в `data`:

1. `username` - имя пользователя.
2. `password` - пароль пользователя.

Создание поста

Отправить POST-запрос на адрес `api/v1/posts/` и передать обязательное поле `text`, в заголовке указать `Authorization: Bearer <токен>`.

1. Пример запроса:

    ```json
    {
        "text": "Мой первый пост."
    }
    ```

2. Пример ответа:

    ```json
    {
        "id": 2,
        "author": "Raul2455",
        "text": "Мой первый пост.",
        "pub_date": "2024-06-17T12:00:22.021094Z",
        "image": null,
        "group": null
    }
    ```

Комментирование поста пользователя

Отправить POST-запрос на адрес `api/v1/posts/{post_id}/comments/` и передать обязательные поля `post` и `text`, в заголовке указать `Authorization: Bearer <токен>`.

1. Пример запроса:

    ```json
    {
        "post": 1,
        "text": "Тест"
    }
    ```

2. Пример ответа:

    ```json
    {
        "id": 1,
        "author": "Raul2455",
        "text": "Тест",
        "created": "2024-06-17T12:06:13.146875Z",
        "post": 1
    }
    ```

# Автор проекта

https://github.com/Raul2455

# Ресурсы

- [Документация проекта](http://127.0.0.1:8000/redoc/)
- [ПО для тестирования API, Postman](https://www.postman.com/)