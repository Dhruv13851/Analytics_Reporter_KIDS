import os

import pandas as pd

from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)

from config import Config


class GA4Service:
    """
    Service class responsible for communicating with
    the Google Analytics Data API.
    """

    def __init__(self):

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = Config.GOOGLE_CREDENTIALS

        self.client = BetaAnalyticsDataClient()
        self.property_id = Config.GA4_PROPERTY_ID

    def _run_report(
        self,
        dimensions: list[str],
        metrics: list[str],
        start_date: str,
        end_date: str,
    ) -> pd.DataFrame:
       

        request = RunReportRequest(
            property=f"properties/{self.property_id}",

            dimensions=[
                Dimension(name=d)
                for d in dimensions
            ],

            metrics=[
                Metric(name=m)
                for m in metrics
            ],

            date_ranges=[
                DateRange(
                    start_date=start_date,
                    end_date=end_date,
                )
            ],
        )

        response = self.client.run_report(request)

        rows = []

        for row in response.rows:

            values = [
                d.value
                for d in row.dimension_values
            ]

            values.extend(
                m.value
                for m in row.metric_values
            )

            rows.append(values)

        columns = dimensions + metrics

        return pd.DataFrame(rows, columns=columns)

    def get_active_users(
        self,
        start_date: str,
        end_date: str,
    ) -> pd.DataFrame:

        return self._run_report(

            dimensions=[
                "date"
            ],

            metrics=[
                "activeUsers",
                "newUsers",
                "totalUsers",
            ],

            start_date=start_date,
            end_date=end_date,
        )

    def get_engagement(
        self,
        start_date: str,
        end_date: str,
    ) -> pd.DataFrame:

        return self._run_report(

            dimensions=[
                "date"
            ],

            metrics=[
                "averageSessionDuration",
                "engagementRate",
                "userEngagementDuration",
            ],

            start_date=start_date,
            end_date=end_date,
        )

    def get_events(
        self,
        start_date: str,
        end_date: str,
    ) -> pd.DataFrame:

        return self._run_report(

            dimensions=[
                "date",
                "eventName",
            ],

            metrics=[
                "eventCount",
                "eventCountPerUser",
            ],

            start_date=start_date,
            end_date=end_date,
        )

    def get_revenue(
        self,
        start_date: str,
        end_date: str,
    ) -> pd.DataFrame:

        return self._run_report(

            dimensions=[
                "date"
            ],

            metrics=[
                "purchaseRevenue",
                "publisherAdClicks",
                "totalRevenue",
            ],

            start_date=start_date,
            end_date=end_date,
        )

    def get_modules(
        self,
        start_date: str,
        end_date: str,
    ) -> pd.DataFrame:

        return self._run_report(

            dimensions=[
                "date",
                "customEvent:module_name",
            ],

            metrics=[
                "eventCount",
                "activeUsers",
            ],

            start_date=start_date,
            end_date=end_date,
        )

    def get_active_users(
        self,
        start_date: str,
        end_date: str,
    ) -> pd.DataFrame:

        return self._run_report(

            dimensions=[
                "date"
            ],

            metrics=[
                "activeUsers",
                "newUsers",
                "totalUsers",
            ],

            start_date=start_date,
            end_date=end_date,
        )
    def get_engagement(
        self,
        start_date,
        end_date,
    ):

        return self._run_report(

            dimensions=[
                "date"
            ],

            metrics=[
                "averageSessionDuration",
                "engagementRate",
                "userEngagementDuration",
            ],

            start_date=start_date,
            end_date=end_date,
        )
    def get_events(
        self,
        start_date,
        end_date,
    ):

        return self._run_report(

            dimensions=[
                "date",
                "eventName",
            ],

            metrics=[
                "eventCount",
                "eventCountPerUser",
            ],

            start_date=start_date,
            end_date=end_date,
        )
    def get_revenue(
        self,
        start_date,
        end_date,
    ):

        return self._run_report(

            dimensions=[
                "date"
            ],

            metrics=[
                "purchaseRevenue",
                "totalAdRevenue",
                "totalRevenue",
            ],


            start_date=start_date,
            end_date=end_date,
        )
    def get_modules(
        self,
        start_date,
        end_date,
    ):

        return self._run_report(

            dimensions=[
                "date",
                "customEvent:module_name",
            ],

            metrics=[
                "eventCount",
                "activeUsers",
            ],

            start_date=start_date,
            end_date=end_date,
        )