def test_database_connection_and_query(db_connection, test_query):
    """
    Тест проверяет:
    1. Успешное подключение к БД (если фикстура db_connection отработала).
    2. Выполнение простейшего SQL-запроса.
    3. Наличие результата.
    """
    with db_connection.cursor() as cursor:
        cursor.execute(test_query)
        result = cursor.fetchone()

    # Проверяем, что запрос вернул хотя бы одну строку
    assert result is not None, "Запрос не вернул результат"

    # Проверяем, что в строке есть данные (для now() это будет объект datetime)
    assert result[0] is not None, "Поле с датой/временем пустое"