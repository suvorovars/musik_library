from sqlalchemy.orm import as_declarative


@as_declarative()
class SqlAlchemyBase:
    # Базовый класс для объектов User и Task
    pass