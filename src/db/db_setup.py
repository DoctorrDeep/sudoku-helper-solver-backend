from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.settings import DB_DRIVER, DB_IP, DB_PORT

Base = declarative_base()
engine = create_engine(f"{DB_DRIVER}://usr:pass@{DB_IP}:{DB_PORT}")
Session = sessionmaker(engine)


def sql_runner():
    # TODO: Make a function that runs the query within a pre-defined context
    # Also, see scoped_session
    with Session.begin() as session:
        print(type(session))
        pass
