Проект для автоматизации тестирования веб-приложения.

Оптимизирован относительно исходного кода, созданного ранее

## Описание

Этот проект предназначен для автоматизации тестирования веб-приложения с использованием Selenium WebDriver и паттерна Page Object.
Проект включает в себя модули для работы с различными страницами веб-приложения, а также вспомогательные функции и конфигурационные файлы.

## Установка

1. **Клонирование репозитория**:
   ```bash
   git clone <URL вашего репозитория>
   cd <имя вашего репозитория>
   ```

2. **Установка зависимостей**:
   Убедитесь, что у вас установлен Python 3.x. Затем установите необходимые зависимости с помощью `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Настройка конфигурационных файлов**:
   Если необходимо, внесите изменения в файл `setting_for_tests.ini`, например:
   ```ini
   [Catalogs]
   directory_with_files_for_analysis = path/to/your/directory

   [Other]
   name_file_with_standarts_results = standart_results.ini
   name_archive_for_analysis = archive_name.zip

   [Setting_project]
   analyzed_languages = python java
   levels_control = 1 2 3 4 5
   name_project = MyProject

   [Credential]
   login = your_login
   password = your_password
   ```

## Использование

### Запуск тестов

Для запуска тестов используйте команду `pytest`:
```bash
pytest
```

### Параметры запуска

Вы можете передать различные параметры через командную строку:
- `--kvs-server`: URL сервера KVS (по умолчанию `127.0.0.1:11000`).
- `--selenium-server`: URL сервера Selenium (по умолчанию `127.0.0.1:4444`).
- `--local-run`: Запуск тестов локально.
- `--headless`: Скрыть браузер.

Пример:
```bash
pytest --kvs-server=http://your-kvs-server --selenium-server=http://your-selenium-server --local-run --headless
```

## Структура проекта

### Директории и файлы

- `common_functions/`: Вспомогательные функции и утилиты.
  - `actions.py`: Вспомогательные функции для работы с веб-элементами.
  - `tools_for_work.py`: Утилиты для работы с файлами и конфигурациями.

- `pages/`: Модули, реализующие паттерн Page Object.
  - `kvs_common.py`: Общие функции для работы с проектом.
  - `authorization_page.py`: Функции для авторизации.
  - `header.py`: Локаторы и функции для работы с заголовком страницы.
  - `projects_page.py`: Функции для работы с проектами.

- `tests/`: Тесты для проверки функциональности веб-приложения.
  - `test_project_page.py`: Тесты для страницы проекта.

- `conftest.py`: Фикстуры и настройки для pytest.
- `requirements.txt`: Список зависимостей проекта.
- `setting_for_tests.ini`: Конфигурационный файл для настройки тестов.
