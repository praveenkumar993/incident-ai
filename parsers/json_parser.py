import json


def parse_json_logs(content):

    data = json.loads(content)

    return data.get(
        "incident_logs",
        []
    )