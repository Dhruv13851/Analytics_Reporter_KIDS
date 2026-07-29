import json
from pathlib import Path
from datetime import date, datetime


class ReportExporter:
    OUTPUT_DIR = Path("output/reports")

    def export_json(self, report, filename=None):

        self.OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        if filename is None:
            filename = (
                f"monthly_report_{report['metadata']['year']}_"
                f"{report['metadata']['month']:02d}.json"
            )

        output_path = self.OUTPUT_DIR / filename

        with output_path.open("w", encoding="utf-8") as f:
            json.dump(
                report,
                f,
                indent=4,
                default=self._json_serializer,
            )

        return str(output_path)

    @staticmethod
    def _json_serializer(obj):
        if isinstance(obj, (date, datetime)):
            return obj.isoformat()

        raise TypeError(f"{type(obj)} is not JSON serializable")