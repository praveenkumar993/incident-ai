from agents.log_analysis_agent import analyze_logs
from tools.log_tool import fetch_logs

print("\n Incident AI System Started\n")

logs = fetch_logs()

analyze_logs(logs)