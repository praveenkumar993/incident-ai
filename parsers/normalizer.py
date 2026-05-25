from parsers.json_parser import (
    parse_json_logs
)

from parsers.csv_parser import (
    parse_csv_logs
)

from parsers.log_parser import (
    parse_raw_logs
)


def normalize_logs(
    filename,
    content
):

    filename = filename.lower()

    if filename.endswith(".json"):

        return parse_json_logs(content)

    elif filename.endswith(".csv"):

        return parse_csv_logs(content)

    elif (
        filename.endswith(".log")
        or
        filename.endswith(".txt")
    ):

        return parse_raw_logs(content)

    return []