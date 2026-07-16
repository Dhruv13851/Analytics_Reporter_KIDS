from sqlalchemy import text

from repositories.base_repository import BaseRepository


class ActiveUserRepository(BaseRepository):

    def save(self, dataframe):

        query = text("""
            INSERT INTO active_users (
                date,
                active_users,
                new_users,
                total_users
            )

            VALUES (
                :date,
                :active_users,
                :new_users,
                :total_users
            )

            ON CONFLICT (date)

            DO UPDATE SET

                active_users = EXCLUDED.active_users,
                new_users = EXCLUDED.new_users,
                total_users = EXCLUDED.total_users;
        """)

        with self.session as session:

            for _, row in dataframe.iterrows():

                session.execute(
                    query,
                    {
                        "date": row["date"],
                        "active_users": int(row["activeUsers"]),
                        "new_users": int(row["newUsers"]),
                        "total_users": int(row["totalUsers"]),
                    },
                )