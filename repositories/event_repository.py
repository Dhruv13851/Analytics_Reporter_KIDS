from sqlalchemy import text

from repositories.base_repository import BaseRepository


class EventRepository(BaseRepository):

    def save(self, dataframe):

        query = text("""
            INSERT INTO events (
                date,
                event_name,
                event_count,
                event_count_per_user
            )

            VALUES (
                :date,
                :event_name,
                :event_count,
                :event_count_per_user
            )

            ON CONFLICT(date, event_name)

            DO UPDATE SET

                event_count = EXCLUDED.event_count,
                event_count_per_user = EXCLUDED.event_count_per_user;
        """)

        with self.session as session:

            for _, row in dataframe.iterrows():

                session.execute(
                    query,
                    {
                        "date": row["date"],
                        "event_name": row["eventName"],
                        "event_count": int(row["eventCount"]),
                        "event_count_per_user": float(row["eventCountPerUser"]),
                    },
                )