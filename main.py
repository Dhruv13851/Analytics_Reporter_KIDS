# from services.etl_manager import ETLManager


# def main():

#     etl = ETLManager()

#     etl.run(

#         start_date="2026-06-13",
#         end_date="2026-07-13",

#     )


# if __name__ == "__main__":
#     main()

# from services.etl_manager import ETLManager
# from services.report_manager import ReportManager


# def main():

#     etl = ETLManager()

#     etl.run(
#         start_date="2026-06-13",
#         end_date="2026-07-13",
#     )

#     report_manager = ReportManager()

#     report = report_manager.generate_monthly_report(
#         year=2026,
#         month=7,
#     )

#     print(report)


# if __name__ == "__main__":
#     main()

from services.etl_manager import ETLManager
from services.report_manager import ReportManager
from services.report_exporter import ReportExporter


def main():

    etl = ETLManager()

    etl.run(
        start_date="2026-06-1",
        end_date="2026-07-13",
    )

    report = ReportManager().generate_monthly_report(
        year=2026,
        month=6,
    )

    exporter = ReportExporter()

    output_path = exporter.export_json(report)

    print(f"\nReport saved to: {output_path}")


if __name__ == "__main__":
    main()