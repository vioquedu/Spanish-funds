"""Settings file where connection to the database is established.
"""

from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from env_file import DATABASE_URL
from data_model.tables import BASE

def database_creation():
    """Create all tables
    """
    engine = create_engine(DATABASE_URL, echo=True)
    BASE.metadata.create_all(engine)

ENGINE = create_engine(DATABASE_URL)
Session = sessionmaker(bind=ENGINE)

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


if __name__ == "__main__":
    database_creation()
