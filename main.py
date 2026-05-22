from tools.log_tool import fetch_logs

from crew.incident_crew import (
    run_incident_crew
)

print("\n Incident AI System Started\n")

logs = fetch_logs()

run_incident_crew(logs)