from ga4_service import GA4Service

from repositories.active_user_repository import ActiveUserRepository
from repositories.engagement_repository import EngagementRepository
from repositories.event_repository import EventRepository
from repositories.module_repository import ModuleRepository
from repositories.revenue_repository import RevenueRepository


class ETLManager:

    def __init__(self):

        self.ga4 = GA4Service()

        self.active_repo = ActiveUserRepository()
        self.engagement_repo = EngagementRepository()
        self.event_repo = EventRepository()
        self.module_repo = ModuleRepository()
        self.revenue_repo = RevenueRepository()

    def run(
        self,
        start_date: str,
        end_date: str,
    ):

        print("=" * 60)
        print("Starting GA4 ETL")
        print("=" * 60)


        print("Fetching Active Users...")

        active_df = self.ga4.get_active_users(
            start_date,
            end_date,
        )

        self.active_repo.save(active_df)

        print(f"{len(active_df)} rows inserted.")


        print("Fetching Engagement...")

        engagement_df = self.ga4.get_engagement(
            start_date,
            end_date,
        )

        self.engagement_repo.save(engagement_df)

        print(f"{len(engagement_df)} rows inserted.")


        print("Fetching Events...")

        event_df = self.ga4.get_events(
            start_date,
            end_date,
        )

        self.event_repo.save(event_df)

        print(f"{len(event_df)} rows inserted.")


        print("Fetching Revenue...")

        revenue_df = self.ga4.get_revenue(
            start_date,
            end_date,
        )

        self.revenue_repo.save(revenue_df)

        print(f"{len(revenue_df)} rows inserted.")


        try:

            print("Fetching Modules...")

            module_df = self.ga4.get_modules(
                start_date,
                end_date,
            )

            self.module_repo.save(module_df)

            print(f"{len(module_df)} rows inserted.")

        except Exception as ex:

            print("Skipping Module ETL")
            print(ex)

        print("=" * 60)
        print("ETL Completed Successfully")
        print("=" * 60)