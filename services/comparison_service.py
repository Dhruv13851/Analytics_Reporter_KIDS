class ComparisonService:


    def calculate_metric_change(
        self,
        current,
        previous
    ):

        difference = current - previous

        if previous == 0:
            percentage = 0
        else:
            percentage = (
                difference / previous
            ) * 100


        return {
            "current": current,
            "previous": previous,
            "difference": difference,
            "percentage_change": round(
                percentage,
                2
            )
        }



    def compare_users(
        self,
        current,
        previous
    ):

        return {

            "average_active_users":
            self.calculate_metric_change(
                current["users"]["average_active_users"],
                previous["users"]["average_active_users"]
            ),


            "total_new_users":
            self.calculate_metric_change(
                current["users"]["total_new_users"],
                previous["users"]["total_new_users"]
            )

        }



    def compare_revenue(
        self,
        current,
        previous
    ):

        return {

            "total_revenue":
            self.calculate_metric_change(
                current["revenue"]["total_revenue"],
                previous["revenue"]["total_revenue"]
            )

        }



    def compare_months(
        self,
        current,
        previous
    ):

        return {

            "users":
            self.compare_users(
                current,
                previous
            ),


            "revenue":
            self.compare_revenue(
                current,
                previous
            )

        }