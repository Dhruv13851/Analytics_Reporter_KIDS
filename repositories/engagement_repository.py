from sqlalchemy import text

from repositories.base_repository import BaseRepository


class EngagementRepository(BaseRepository):

    def save(self, dataframe):

        query = text("""
            INSERT INTO engagement (
                date,
                avg_session_duration,
                engagement_rate,
                user_engagement_duration
            )

            VALUES (
                :date,
                :avg_session_duration,
                :engagement_rate,
                :user_engagement_duration
            )

            ON CONFLICT(date)

            DO UPDATE SET

                avg_session_duration = EXCLUDED.avg_session_duration,
                engagement_rate = EXCLUDED.engagement_rate,
                user_engagement_duration = EXCLUDED.user_engagement_duration;
        """)

        with self.session as session:

            for _, row in dataframe.iterrows():

                session.execute(
                    query,
                    {
                        "date": row["date"],
                        "avg_session_duration": float(row["averageSessionDuration"]),
                        "engagement_rate": float(row["engagementRate"]),
                        "user_engagement_duration": float(row["userEngagementDuration"]),
                    },
                )