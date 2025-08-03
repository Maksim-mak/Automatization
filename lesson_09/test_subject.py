import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Subject

# Замените значения на ваши действительные учетные данные
db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"


@pytest.fixture(scope='module')
def test_setup():
    # Создание базы данных и таблицы
    engine = create_engine(db_connection_string)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    yield session  # Возвращаем сессию для использования в тестах

    # Удаление таблицы после тестов
    Base.metadata.drop_all(engine)
    session.close()


def test_add_subject(test_setup):
    session = test_setup

    # Добавление нового предмета
    new_subject = Subject(name='Mathematics')
    session.add(new_subject)
    session.commit()

    # Проверка, что предмет добавлен
    assert new_subject.id is not None  # ID должен быть сгенерирован
    saved_subject = (session.query(Subject).
                     filter_by(name='Mathematics').first())
    assert saved_subject is not None
    assert saved_subject.name == 'Mathematics'


def test_update_subject(test_setup):
    session = test_setup

    # Обновление предмета
    subject_to_update = (session.query
                         (Subject).filter_by(name='Mathematics').first())
    subject_to_update.name = 'Advanced Mathematics'
    session.commit()

    # Проверка, что предмет обновлен
    updated_subject = (session.query(Subject).
                       filter_by(id=subject_to_update.id).first())
    assert updated_subject.name == 'Advanced Mathematics'


def test_delete_subject(test_setup):
    session = test_setup

    # Удаление предмета
    subject_to_delete = (session.query(Subject).
                         filter_by(name='Advanced Mathematics').first())
    session.delete(subject_to_delete)
    session.commit()

    # Проверка, что предмет удален
    deleted_subject = (session.query(Subject).
                       filter_by(id=subject_to_delete.id).first())
    assert deleted_subject is None
