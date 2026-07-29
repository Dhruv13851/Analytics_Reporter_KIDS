from pydantic import BaseModel


class MetricComparison(BaseModel):

    current: float

    previous: float

    difference: float

    percentage_change: float



class UserComparison(BaseModel):

    average_active_users: MetricComparison

    total_new_users: MetricComparison



class RevenueComparison(BaseModel):

    total_revenue: MetricComparison



class ComparisonReport(BaseModel):

    users: UserComparison

    revenue: RevenueComparison