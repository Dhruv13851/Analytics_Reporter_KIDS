from sqlalchemy import text

from repositories.base_repository import BaseRepository


class ModuleRepository(BaseRepository):

    def save(self, dataframe):

        query = text("""
            INSERT INTO modules (
                date,
                module_name,
                event_count,
                total_users
            )

            VALUES (
                :date,
                :module_name,
                :event_count,
                :total_users
            )

            ON CONFLICT(date, module_name)

            DO UPDATE SET

                event_count = EXCLUDED.event_count,
                total_users = EXCLUDED.total_users;
        """)

        with self.session as session:

            for _, row in dataframe.iterrows():

                session.execute(
                    query,
                    {
                        "date": row["date"],
                        "module_name": row["customEvent:module_name"],
                        "event_count": int(row["eventCount"]),
                        "total_users": int(row["activeUsers"]),
                    },
                )