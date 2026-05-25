import re


def parse_raw_logs(content):

    logs = []

    lines = content.splitlines()

    pattern = re.compile(

        r".*?(ERROR|WARNING|CRITICAL|INFO)\s+([\w-]+)\s+(.*)"
    )

    for line in lines:

        match = pattern.match(line)

        if match:

            severity, service, message = match.groups()

            severity = severity.lower()

            if severity == "warning":
                severity = "medium"

            elif severity == "error":
                severity = "high"

            elif severity == "critical":
                severity = "critical"

            logs.append({

                "service": service,

                "severity": severity,

                "message": message
            })

    return logs