import sqlite3
from pprint import pprint


def execute_query(query_number, query_file):
    try:
        connection = sqlite3.connect('hw_module_6')
        cursor = connection.cursor()

        # Читаємо SQL-запит з файлу
        with open(query_file, 'r') as file:
            sql_query = file.read()

        # print(f"\nExecuting Query {sql_query}")

        # Виконуємо SQL-запит
        cursor.execute(sql_query)

        # Отримуємо результати (якщо потрібно)
        result = cursor.fetchall()

        # Зберігаємо зміни у базі даних
        connection.commit()

        print(f"\nQuery {query_number} result:")
        for row in result:
            pprint(row)

    except sqlite3.Error as error:
        pprint(error)

    finally:
        # Закриваємо з'єднання
        connection.close()


# Виконуємо SQL-запити
execute_query(1, 'query_1.sql')
execute_query(2, 'query_2.sql')
execute_query(3, 'query_3.sql')
execute_query(4, 'query_4.sql')
execute_query(5, 'query_5.sql')
execute_query(6, 'query_6.sql')
execute_query(7, 'query_7.sql')
execute_query(8, 'query_8.sql')
execute_query(9, 'query_9.sql')
execute_query(10, 'query_10.sql')
execute_query(11, 'query_11.sql')
execute_query(12, 'query_12.sql')
