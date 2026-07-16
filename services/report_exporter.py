import json
from pathlib import Path
from datetime import date, datetime


class ReportExporter:
    OUTPUT_DIR = Path("output/reports")

    def export_json(self, report: dict) -> Path:
        self.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        metadata = report["metadata"]

        filename = (
            f"monthly_report_{metadata['year']}_{metadata['month']:02d}.json"
        )

        output_file = self.OUTPUT_DIR / filename

        with output_file.open("w", encoding="utf-8") as f:
            json.dump(
                report,
                f,
                indent=4,
                default=self._json_serializer,
            )

        return output_file

    @staticmethod
    def _json_serializer(obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()

        raise TypeError(f"{type(obj)} is not JSON serializable")