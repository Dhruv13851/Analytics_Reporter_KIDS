from services.etl_manager import ETLManager
from services.report_manager import ReportManager
from services.report_exporter import ReportExporter
from services.comparison_service import ComparisonService
from services.llm_service import LLMService


def main():

    etl = ETLManager()

    etl.run(
        start_date="2026-06-01",
        end_date="2026-07-27",
    )

    report_manager = ReportManager()

    current_report = report_manager.generate_monthly_report(
        year=2026,
        month=7,
    )

    previous_report = report_manager.generate_monthly_report(
        year=2026,
        month=6,
    )

   
    comparison_service = ComparisonService()

    comparison = comparison_service.compare_months(
        current=current_report,
        previous=previous_report,
    )

   
    llm_service = LLMService()

    ai_analysis = llm_service.analyze(comparison)


    exporter = ReportExporter()

    exporter.export_json(
        current_report,
        filename="monthly_report_2026_07.json",
    )

    exporter.export_json(
        previous_report,
        filename="monthly_report_2026_06.json",
    )

    exporter.export_json(
        comparison,
        filename="comparison_2026_07_vs_2026_06.json",
    )

    exporter.export_json(
        ai_analysis,
        filename="ai_analysis_2026_07.json",
    )


if __name__ == "__main__":
    main()