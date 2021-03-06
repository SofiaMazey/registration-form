import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlalchemy.ext.declarative as dec


def global_init(db_file):
    global __factory

    if __factory:
        return

    if not db_file or not db_file.strip():
        raise Exception("Необходимо указать файл базы данных.")

    conn_str = f'sqlite:///{db_file.strip()}?check_same_thread=False'
    print(f"Подключение к базе данных по адресу {conn_str}")

    engine = sa.create_engine(conn_str, echo=False)
    __factory = orm.sessionmaker(bind=engine)

    from . import __all_models

    SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    global __factory
    return __factory()


def set_password(self, password):  # устанавливает значение хэша
    self.hashed_password = generate_password_hash(password)


def check_password(self, password):  # проверка введенного пароля
    return check_password_hash(self.hashed_password, password)


SqlAlchemyBase = dec.declarative_base()

__factory = None