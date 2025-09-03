from sqlalchemy import create_engine, inspect, text


db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)


def test_db_connection():
    inspector = inspect(db)
    names = inspector.get_table_names()
    print(names)  # Для отладки
    assert 'app_users' in names  # Проверяем наличие таблицы

def test_select():
    connection = db.connect()
    result = connection.execute(text("SELECT * FROM company"))
    rows = result.mappings().all()
    row1 = rows[0]

    assert row1['id'] == 1
    assert row1['name'] == "QA Студия 'ТестировщикЪ'"

    connection.close()

def test_select_1_row():
    connection = db.connect()
    sql_statement = text("SELECT * FROM company WHERE id = :company_id")
    result = connection.execute(sql_statement, {"company_id": 1})
    rows = result.mappings().all()

    assert len(rows) == 1
    assert rows[0]["name"] == "QA Студия 'ТестировщикЪ'"

    connection.close()


def test_select_1_row_with_two_filters():
    with db.connect() as connection:
        sql_statement = text("SELECT * FROM company "
                             "WHERE is_active = :is_active AND id >= :id")
        result = connection.execute(sql_statement, {"id": 65, "is_active": True})
        rows = result.mappings().all()

        print(f"Number of rows returned: {len(rows)}")  # Для отладки
        print(rows)  # Выводим строки для анализа

        assert len(rows) == 46  # Возможно, нужно изменить это значение

