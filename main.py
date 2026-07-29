from services.etl_manager import ETLManager
from services.report_manager import ReportManager
from services.report_exporter import ReportExporter
from services.comparison_service import ComparisonService


def main():

    # --------------------------------------------------
    # Step 1: Run ETL (Optional)
    # --------------------------------------------------
    etl = ETLManager()

    etl.run(
        start_date="2026-06-01",
        end_date="2026-07-27",
    )

    # --------------------------------------------------
    # Step 2: Generate Monthly Reports
    # --------------------------------------------------
    report_manager = ReportManager()

    current_report = report_manager.generate_monthly_report(
        year=2026,
        month=7,
    )

    previous_report = report_manager.generate_monthly_report(
        year=2026,
        month=6,
    )

    # --------------------------------------------------
    # Step 3: Export Monthly Reports (Optional)
    # --------------------------------------------------
    exporter = ReportExporter()

    current_report_path = exporter.export_json(current_report)
    previous_report_path = exporter.export_json(previous_report)

    print(f"Current report saved to: {current_report_path}")
    print(f"Previous report saved to: {previous_report_path}")

    # --------------------------------------------------
    # Step 4: Generate Comparison
    # --------------------------------------------------
    comparison_service = ComparisonService()

    comparison = comparison_service.compare_months(
        current=current_report,
        previous=previous_report,
    )

    comparison_path = exporter.export_json(
        comparison,
        filename="comparison_2026_07_vs_2026_06.json",
    )

    print(f"Comparison saved to: {comparison_path}")


if __name__ == "__main__":
    main()