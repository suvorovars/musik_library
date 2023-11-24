from tokenize import String

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, as_declarative


# переменная, которая хранит фабрику сессий базы данных
__factory = None

# Переменная, которая хранит коннект
__connection = None


def global_init(db_file: String) -> None:
    """
    Функция используется для инициализации подключения к базе данных и фабрики сессий.
    """
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать файл базы данных.")

    conn_str = db_file  # Можно отредактировать, для использования с базами данных других типов
    print(f"Подключение к базе данных по адресу {conn_str}")

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)


    from .tables import __all_models
    from .tables.default import SqlAlchemyBase

    SqlAlchemyBase.metadata.create_all(engine)

    global __connection
    __connection = engine.connect


def create_session() -> Session:
    """
    Функция возвращает новую сессию SQLAlchemy, созданную из глобальной фабрики сессий
    """
    global __factory
    return __factory()


def create_connection() -> 'Connection':
    """
    Функция возращает новый Коннект SQLAlchemy
    """
    global __connection
    return __connection()