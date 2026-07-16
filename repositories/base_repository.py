from database import Database


class BaseRepository:
    """Base repository providing a database session."""

    @property
    def session(self):
        return Database.get_session()