# Автотест подключения к PostgreSQL

Автотест на pytest, проверяющий доступность БД PostgreSQL и выполнение
простейшего запроса.

## Требования

- Python 3.11+
- PostgreSQL 15+
- Зависимости из requirements.txt
  
## Структура проекта

```
.
├── README.md
├── requirements.txt
├── test_db_connection.py
├── conftest.py
├── gitignore
└── screenshots/
    └── screenshots.pdf
```

## Настройка окружения

1. Установите зависимости:

   ```bash
   python -m venv .venv
   source .venv/bin/activate 
   pip install -r requirements.txt
   ```

## Запуск тестов

```bash
pytest -v
```

Запуск только тестов БД:

```bash
pytest db_connection_tests/test_db_connection.py.py -v
```
                   |

## Поведение при недоступной БД

Если БД недоступна, тесты падают  с понятным сообщением об ошибке
подключения. 

## Критерии приёмки

- [ ] pytest проходит на чистом окружении
- [ ] при остановленной БД тест корректно падает с читаемым сообщением
- [ ] секреты не попадают в репозиторий
- [ ] тесты не имеют побочных эффектов в БД 
- [ ] время выполнения < 5 сек


## Контакты

Ответственный: `Демченко Карина, happiness00kk@gmail.com`
