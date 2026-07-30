class ComparisonService:

    def calculate_metric_change(
        self,
        current,
        previous
    ):

        current = current or 0
        previous = previous or 0

        difference = current - previous

        if previous == 0:
            percentage = 0 if current == 0 else 100
        else:
            percentage = (difference / previous) * 100

        return {
            "current": current,
            "previous": previous,
            "difference": difference,
            "percentage_change": round(
                percentage,
                2
            )
        }

    def compare_numeric_section(
        self,
        current_section,
        previous_section
    ):

        comparison = {}

        previous_section = previous_section or {}

        for metric_name, current_value in current_section.items():

            if not isinstance(
                current_value,
                (int, float)
            ):
                continue

            comparison[metric_name] = (
                self.calculate_metric_change(
                    current_value,
                    previous_section.get(
                        metric_name,
                        0
                    )
                )
            )

        return comparison

    def compare_ranked_items(
        self,
        current_items,
        previous_items,
        name_key
    ):

        comparison = {}

        previous_lookup = {
            item[name_key]: item
            for item in previous_items
        }

        current_lookup = {
            item[name_key]: item
            for item in current_items
        }

        all_names = (
            set(current_lookup.keys())
            | set(previous_lookup.keys())
        )

        for name in sorted(all_names):

            current_item = current_lookup.get(
                name,
                {}
            )

            previous_item = previous_lookup.get(
                name,
                {}
            )

            item_comparison = {}

            # Get every numeric metric
            # available for this item.
            metric_names = (
                set(current_item.keys())
                | set(previous_item.keys())
            )

            for metric_name in sorted(metric_names):

                if metric_name == name_key:
                    continue

                current_value = current_item.get(
                    metric_name,
                    0
                )

                previous_value = previous_item.get(
                    metric_name,
                    0
                )

                if not isinstance(
                    current_value,
                    (int, float)
                ):
                    continue

                item_comparison[metric_name] = (
                    self.calculate_metric_change(
                        current_value,
                        previous_value
                    )
                )

            comparison[name] = item_comparison

        return comparison

    def compare_months(
        self,
        current,
        previous
    ):

        previous = previous or {}

        comparison = {}

        # ---------------------------
        # Numeric summaries
        # ---------------------------

        numeric_sections = [
            "users",
            "engagement",
            "revenue",
        ]

        for section in numeric_sections:

            if section in current:

                comparison[section] = (
                    self.compare_numeric_section(
                        current[section],
                        previous.get(
                            section,
                            {}
                        )
                    )
                )

        # ---------------------------
        # Event Summary
        # ---------------------------

        if (
            "events" in current
            and "top_events" in current["events"]
        ):

            comparison["events"] = {

                "top_events":
                self.compare_ranked_items(
                    current["events"]["top_events"],
                    previous
                    .get("events", {})
                    .get("top_events", []),
                    name_key="event_name"
                )

            }

        # ---------------------------
        # Module Summary
        # ---------------------------

        if (
            "modules" in current
            and "top_modules" in current["modules"]
        ):

            comparison["modules"] = {

                "top_modules":
                self.compare_ranked_items(
                    current["modules"]["top_modules"],
                    previous
                    .get("modules", {})
                    .get("top_modules", []),
                    name_key="module_name"
                )

            }

        return comparison