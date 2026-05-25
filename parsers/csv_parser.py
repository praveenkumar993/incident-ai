import csv
import io


def parse_csv_logs(content):

    logs = []

    reader = csv.DictReader(
        io.StringIO(content)
    )

    for row in reader:

        logs.append({

            "service":
                row.get("service", ""),

            "severity":
                row.get("severity", "").lower(),

            "message":
                row.get("message", "")
        })

    return logs