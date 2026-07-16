from sqlalchemy import text

from repositories.base_repository import BaseRepository


class RevenueRepository(BaseRepository):

    def save(self, dataframe):

        query = text("""
            INSERT INTO revenue (
                date,
                purchase_revenue,
                ad_revenue,
                total_revenue
            )

            VALUES (
                :date,
                :purchase_revenue,
                :ad_revenue,
                :total_revenue
            )

            ON CONFLICT(date)

            DO UPDATE SET

                purchase_revenue = EXCLUDED.purchase_revenue,
                ad_revenue = EXCLUDED.ad_revenue,
                total_revenue = EXCLUDED.total_revenue;
        """)

        with self.session as session:

            for _, row in dataframe.iterrows():

                session.execute(
                    query,
                    {
                        "date": row["date"],
                        "purchase_revenue": float(row["purchaseRevenue"]),
                        "ad_revenue": float(row["totalAdRevenue"]),
                        "total_revenue": float(row["totalRevenue"]),
                    },
                )