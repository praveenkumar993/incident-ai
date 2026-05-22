import requests

def fetch_logs():

    response = requests.get(
        "http://127.0.0.1:8000/logs"
    )

    data = response.json()

    return data["incident_logs"]