# Weather Forecast Web Application

## Описание
Веб-приложение, где пользователь вводит название города и получает прогноз погоды в этом городе на ближайшее время.

## Функциональность
- Ввод города и получение прогноза погоды.
- Автодополнение при вводе города.
- API для получения статистики запросов.

## Технологии
- Django
- Open Meteo API
- SQLite
- Docker

## Запуск
1. Клонируйте репозиторий.
2. Создайте виртуальное окружение и установите зависимости:
    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
3. Запустите миграции:
    ```bash
    python manage.py migrate
    ```
4. Запустите сервер:
    ```bash
    python manage.py runserver
    ```
5. Для запуска в Docker используйте:
    ```bash
    docker-compose up --build
    ```

