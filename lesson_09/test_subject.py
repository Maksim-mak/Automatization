import pytest
import psycopg2

# Замените значения на ваши действительные учетные данные
db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"


@pytest.fixture(scope='module')
def db_connection():
    connection = psycopg2.connect(db_connection_string)
    cursor = connection.cursor()

    # Создание таблицы Subject для тестов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS subjects (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        );
    ''')
    connection.commit()

    yield cursor, connection
    # Возвращаем cursor и connection для использования в тестах

    # Удаление таблицы после тестов
    cursor.execute('DROP TABLE IF EXISTS subjects;')
    connection.commit()
    cursor.close()
    connection.close()


def test_add_subject(db_connection):
    cursor, connection = db_connection

    # Добавление нового предмета
    (cursor.execute
     ("INSERT INTO subjects (name) VALUES (%s) RETURNING id;",
      ('Mathematics',)))
    subject_id = cursor.fetchone()[0]
    connection.commit()

    # Проверка, что предмет добавлен
    assert subject_id is not None  # ID должен быть сгенерирован
    cursor.execute("SELECT name FROM subjects WHERE id = %s;", (subject_id,))
    saved_subject = cursor.fetchone()
    assert saved_subject is not None
    assert saved_subject[0] == 'Mathematics'


def test_update_subject(db_connection):
    cursor, connection = db_connection

    # Обновление предмета
    cursor.execute("UPDATE subjects SET name = %s WHERE name = %s;",
                   ('Advanced Mathematics', 'Mathematics'))
    connection.commit()

    # Проверка, что предмет обновлен
    cursor.execute("SELECT name FROM subjects WHERE name = %s;",
                   ('Advanced Mathematics',))
    updated_subject = cursor.fetchone()
    assert updated_subject is not None
    assert updated_subject[0] == 'Advanced Mathematics'


def test_delete_subject(db_connection):
    cursor, connection = db_connection

    # Удаление предмета
    cursor.execute("DELETE FROM subjects WHERE name = %s;",
                   ('Advanced Mathematics',))
    connection.commit()

    # Проверка, что предмет удален
    cursor.execute("SELECT * FROM subjects WHERE name = %s;",
                   ('Advanced Mathematics',))
    deleted_subject = cursor.fetchone()
    assert deleted_subject is None
