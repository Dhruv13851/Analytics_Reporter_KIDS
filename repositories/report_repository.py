# from datetime import date

# from sqlalchemy import text

# from repositories.base_repository import BaseRepository


# class ReportRepository(BaseRepository):

#     def get_user_summary(
#         self,
#         start_date: date,
#         end_date: date,
#     ) -> dict:

#         query = text("""
#             SELECT
#                 AVG(active_users) AS average_active_users,
#                 MAX(active_users) AS peak_active_users,
#                 SUM(new_users) AS total_new_users,

#                 (
#                     SELECT total_users
#                     FROM active_users
#                     WHERE date BETWEEN :start_date AND :end_date
#                     ORDER BY date DESC
#                     LIMIT 1
#                 ) AS last_day_total_users

#             FROM active_users

#             WHERE date BETWEEN :start_date AND :end_date;
#         """)

#         with self.session as session:

#             row = session.execute(
#                 query,
#                 {
#                     "start_date": start_date,
#                     "end_date": end_date,
#                 },
#             ).mappings().one()

#             return {
#                 "average_active_users": float(row["average_active_users"] or 0),
#                 "peak_active_users": int(row["peak_active_users"] or 0),
#                 "total_new_users": int(row["total_new_users"] or 0),
#                 "last_day_total_users": int(row["last_day_total_users"] or 0),
#             }

#     def get_revenue_summary(
#         self,
#         start_date: date,
#         end_date: date,
#     ) -> dict:

#         query = text("""
#             SELECT

#                 SUM(purchase_revenue) AS purchase_revenue,
#                 SUM(ad_revenue) AS ad_revenue,
#                 SUM(total_revenue) AS total_revenue

#             FROM revenue

#             WHERE date BETWEEN :start_date AND :end_date;
#         """)

#         with self.session as session:

#             row = session.execute(
#                 query,
#                 {
#                     "start_date": start_date,
#                     "end_date": end_date,
#                 },
#             ).mappings().one()

#             return {
#                 "purchase_revenue": float(row["purchase_revenue"] or 0),
#                 "ad_revenue": float(row["ad_revenue"] or 0),
#                 "total_revenue": float(row["total_revenue"] or 0),
#             }

#     def get_engagement_summary(
#         self,
#         start_date: date,
#         end_date: date,
#     ) -> dict:

#         query = text("""
#             SELECT

#                 AVG(avg_session_duration) AS average_session_duration,
#                 AVG(engagement_rate) AS average_engagement_rate,
#                 SUM(user_engagement_duration) AS total_user_engagement_duration

#             FROM engagement

#             WHERE date BETWEEN :start_date AND :end_date;
#         """)

#         with self.session as session:

#             row = session.execute(
#                 query,
#                 {
#                     "start_date": start_date,
#                     "end_date": end_date,
#                 },
#             ).mappings().one()

#             return {
#                 "average_session_duration": float(
#                     row["average_session_duration"] or 0
#                 ),
#                 "average_engagement_rate": float(
#                     row["average_engagement_rate"] or 0
#                 ),
#                 "total_user_engagement_duration": float(
#                     row["total_user_engagement_duration"] or 0
#                 ),
#             }

#     def get_event_summary(
#         self,
#         start_date: date,
#         end_date: date,
#         top_n: int = 10,
#     ) -> dict:

#         total_query = text("""
#             SELECT
#                 SUM(event_count) AS total_events

#             FROM events

#             WHERE date BETWEEN :start_date AND :end_date;
#         """)

#         top_query = text("""
#             SELECT

#                 event_name,
#                 SUM(event_count) AS event_count

#             FROM events

#             WHERE date BETWEEN :start_date AND :end_date

#             GROUP BY event_name

#             ORDER BY event_count DESC

#             LIMIT :top_n;
#         """)

#         with self.session as session:

#             total_events = session.execute(
#                 total_query,
#                 {
#                     "start_date": start_date,
#                     "end_date": end_date,
#                 },
#             ).scalar()

#             top_events = session.execute(
#                 top_query,
#                 {
#                     "start_date": start_date,
#                     "end_date": end_date,
#                     "top_n": top_n,
#                 },
#             ).mappings().all()

#             return {
#                 "total_events": int(total_events or 0),
#                 "top_events": [dict(row) for row in top_events],
#             }

#     def get_module_summary(
#         self,
#         start_date: date,
#         end_date: date,
#         top_n: int = 10,
#     ) -> dict:

#         total_query = text("""
#             SELECT

#                 SUM(event_count) AS total_module_events

#             FROM modules

#             WHERE date BETWEEN :start_date AND :end_date;
#         """)

#         top_query = text("""
#             SELECT

#                 module_name,
#                 SUM(event_count) AS event_count,
#                 SUM(total_users) AS total_users

#             FROM modules

#             WHERE date BETWEEN :start_date AND :end_date

#             GROUP BY module_name

#             ORDER BY event_count DESC

#             LIMIT :top_n;
#         """)

#         with self.session as session:

#             total_events = session.execute(
#                 total_query,
#                 {
#                     "start_date": start_date,
#                     "end_date": end_date,
#                 },
#             ).scalar()

#             top_modules = session.execute(
#                 top_query,
#                 {
#                     "start_date": start_date,
#                     "end_date": end_date,
#                     "top_n": top_n,
#                 },
#             ).mappings().all()

#             return {
#                 "total_module_events": int(total_events or 0),
#                 "top_modules": [dict(row) for row in top_modules],
#             }

from datetime import date

from sqlalchemy import text

from repositories.base_repository import BaseRepository


class ReportRepository(BaseRepository):

    def get_user_summary(
        self,
        start_date: date,
        end_date: date,
    ) -> dict:

        query = text("""
            SELECT
                AVG(active_users) AS average_active_users,
                MAX(active_users) AS peak_active_users,
                SUM(new_users) AS total_new_users,

                (
                    SELECT total_users
                    FROM active_users
                    WHERE date BETWEEN :start_date AND :end_date
                    ORDER BY date DESC
                    LIMIT 1
                ) AS last_day_total_users

            FROM active_users

            WHERE date BETWEEN :start_date AND :end_date;
        """)

        with self.session as session:

            row = session.execute(
                query,
                {
                    "start_date": start_date,
                    "end_date": end_date,
                },
            ).mappings().one()

            return {
                "average_active_users": float(
                    row["average_active_users"] or 0
                ),
                "peak_active_users": int(
                    row["peak_active_users"] or 0
                ),
                "total_new_users": int(
                    row["total_new_users"] or 0
                ),
                "last_day_total_users": int(
                    row["last_day_total_users"] or 0
                ),
            }

    def get_revenue_summary(
        self,
        start_date: date,
        end_date: date,
    ) -> dict:

        query = text("""
            SELECT
                SUM(purchase_revenue) AS purchase_revenue,
                SUM(ad_revenue) AS ad_revenue,
                SUM(total_revenue) AS total_revenue

            FROM revenue

            WHERE date BETWEEN :start_date AND :end_date;
        """)

        with self.session as session:

            row = session.execute(
                query,
                {
                    "start_date": start_date,
                    "end_date": end_date,
                },
            ).mappings().one()

            return {
                "purchase_revenue": float(
                    row["purchase_revenue"] or 0
                ),
                "ad_revenue": float(
                    row["ad_revenue"] or 0
                ),
                "total_revenue": float(
                    row["total_revenue"] or 0
                ),
            }

    def get_engagement_summary(
        self,
        start_date: date,
        end_date: date,
    ) -> dict:

        query = text("""
            SELECT
                AVG(avg_session_duration) AS average_session_duration,
                AVG(engagement_rate) AS average_engagement_rate,
                SUM(user_engagement_duration) AS total_user_engagement_duration

            FROM engagement

            WHERE date BETWEEN :start_date AND :end_date;
        """)

        with self.session as session:

            row = session.execute(
                query,
                {
                    "start_date": start_date,
                    "end_date": end_date,
                },
            ).mappings().one()

            return {
                "average_session_duration": float(
                    row["average_session_duration"] or 0
                ),
                "average_engagement_rate": float(
                    row["average_engagement_rate"] or 0
                ),
                "total_user_engagement_duration": float(
                    row["total_user_engagement_duration"] or 0
                ),
            }

    def get_event_summary(
        self,
        start_date: date,
        end_date: date,
        top_n: int = 10,
    ) -> dict:

        total_query = text("""
            SELECT
                SUM(event_count) AS total_events

            FROM events

            WHERE date BETWEEN :start_date AND :end_date;
        """)

        top_query = text("""
            SELECT
                event_name,
                SUM(event_count) AS event_count

            FROM events

            WHERE date BETWEEN :start_date AND :end_date

            GROUP BY event_name

            ORDER BY event_count DESC

            LIMIT :top_n;
        """)

        with self.session as session:

            total_events = session.execute(
                total_query,
                {
                    "start_date": start_date,
                    "end_date": end_date,
                },
            ).scalar()

            top_events = session.execute(
                top_query,
                {
                    "start_date": start_date,
                    "end_date": end_date,
                    "top_n": top_n,
                },
            ).mappings().all()

            return {
                "total_events": int(total_events or 0),
                "top_events": [dict(row) for row in top_events],
            }

    def get_module_summary(
        self,
        start_date: date,
        end_date: date,
        top_n: int = 10,
    ) -> dict:

        total_query = text("""
            SELECT
                SUM(event_count) AS total_module_events

            FROM modules

            WHERE date BETWEEN :start_date AND :end_date
                AND module_name != '(not set)';
        """)
        top_query = text("""
            SELECT
                module_name,

                SUM(event_count) AS event_count,

                SUM(total_users) AS total_users,

                AVG(total_users) AS average_daily_users

            FROM modules

            WHERE date BETWEEN :start_date AND :end_date
                AND module_name != '(not set)'
                AND module_name != '(other)'

            GROUP BY module_name

            ORDER BY event_count DESC

            LIMIT :top_n;
        """)
        # top_query = text("""
        #     SELECT
        #         module_name,
        #         SUM(event_count) AS event_count,
        #         SUM(total_users) AS total_users

        #     FROM modules

        #     WHERE date BETWEEN :start_date AND :end_date
        #         AND module_name != '(not set)' 

        #     GROUP BY module_name

        #     ORDER BY event_count DESC

        #     LIMIT :top_n;
        # """)

        with self.session as session:

            total_events = session.execute(
                total_query,
                {
                    "start_date": start_date,
                    "end_date": end_date,
                },
            ).scalar()

            top_modules = session.execute(
                top_query,
                {
                    "start_date": start_date,
                    "end_date": end_date,
                    "top_n": top_n,
                },
            ).mappings().all()

            return {
                    "total_module_events": int(total_events or 0),
                    "top_modules": [
                        {
                            "module_name": row["module_name"],
                            "event_count": int(row["event_count"] or 0),
                            "total_users": int(row["total_users"] or 0),
                            "average_daily_users": float(
                                row["average_daily_users"] or 0
                            ),
                        }
                        for row in top_modules
                    ],
        }