from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config


class Database:
    """
    Handles PostgreSQL connection, session management,
    and transaction handling.
    """

    _engine = None
    _SessionFactory = None

    @classmethod
    def initialize(cls):
      

        if cls._engine is None:

            cls._engine = create_engine(
                Config.DATABASE_URL,

                pool_size=10,
                max_overflow=20,
                pool_pre_ping=True,
                pool_recycle=3600,

                future=True,

                echo=False
            )

            cls._SessionFactory = sessionmaker(
                bind=cls._engine,
                autoflush=False,
                autocommit=False,
                expire_on_commit=False,
            )

    @classmethod
    @contextmanager
    def get_session(cls):
      

        if cls._engine is None:
            cls.initialize()

        session = cls._SessionFactory()

        try:
            yield session
            session.commit()

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()