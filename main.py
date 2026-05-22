from tools.log_tool import fetch_logs

from crew.incident_crew import (
    run_incident_crew
)

print("\n" + "="*60)
print(" INCIDENT AI SYSTEM STARTED ")
print("="*60)

logs = fetch_logs()

result = run_incident_crew(logs)

final_report = str(result)

final_report = final_report.replace("[Date]", "")
final_report = final_report.replace("[Time]", "")
final_report = final_report.replace("On ,", "")

print("\n" + "="*60)
print(" FINAL INCIDENT REPORT ")
print("="*60)

print(final_report)