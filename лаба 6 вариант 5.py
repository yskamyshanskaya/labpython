#лаб 6 вариант 5
#Написать функцию, которая принимает словарь, в котором ключами являются наименования таблиц, а значениями
#список списков, содержащих данные для таблицы, и выполняет
#вставку полученных данных в указанные таблицы.

import sqlite3

def insert_data_into_tables(data_dict, database_path):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        for table_name, data_rows in data_dict.items():
            for row in data_rows:
                placeholders = ', '.join(['?'] * len(row))
                insert_query = f'INSERT INTO {table_name} VALUES ({placeholders})'
                cursor.execute(insert_query, row)

            conn.commit()
            conn.close()
            return True
    except Exception as e:
             print(f"Ошибка при вставке данных: {str(e)}")
             return False
 # Пример использования функции
data_dict = {
    'table1': [(1, 'John'), (2, 'Alice')],
    'table2': [(101, 'Apple'), (102, 'Banana')],
}
database_path = 'my_database.db' # Замените на путь к вашей SQLite базе данных
result = insert_data_into_tables(data_dict, database_path)

if result:
    print("Данные успешно вставлены в таблицы.")
else:
    print("Ошибка при вставке данных.")