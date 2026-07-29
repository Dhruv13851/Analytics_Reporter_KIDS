from calendar import monthrange
from datetime import date, datetime

from repositories.report_repository import ReportRepository


class ReportManager:

    def __init__(self):
        self.report_repository = ReportRepository()

    def generate_monthly_report(
        self,
        year: int,
        month: int,
    ) -> dict:
        """
        Generate a complete monthly report.

        Args:
            year: Report year.
            month: Report month.

        Returns:
            Dictionary containing all report sections.
        """

        start_date = date(year, month, 1)

        end_date = date(
            year,
            month,
            monthrange(year, month)[1],
        )

        report = {
            "metadata": {
                "year": year,
                "month": month,
                "start_date": start_date,
                "end_date": end_date,
                "generated_at": datetime.utcnow(),
            },

            "users": self.report_repository.get_user_summary(
                start_date,
                end_date,
            ),

            "engagement": self.report_repository.get_engagement_summary(
                start_date,
                end_date,
            ),

            "revenue": self.report_repository.get_revenue_summary(
                start_date,
                end_date,
            ),

            "events": self.report_repository.get_event_summary(
                start_date,
                end_date,
            ),

            "modules": self.report_repository.get_module_summary(
                start_date,
                end_date,
            ),
        }

        return report