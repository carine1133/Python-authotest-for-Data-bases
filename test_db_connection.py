def test_database_connection_and_query(db_connection, test_query):
    with db_connection.cursor() as cursor:
        cursor.execute(test_query)
        result = cursor.fetchone()

    assert result is not None, "запрос не вернул результат"

    assert result[0] is not None, "поле с датой или временем пустое"
