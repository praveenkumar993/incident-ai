from crewai import Agent

log_analysis_agent = Agent(
    role="Log Analysis Specialist",

    goal="""
    Analyze incident logs and identify critical system failures
    """,

    backstory="""
    You are an expert SRE engineer specializing in 
    distributed systems, production monitoring, 
    and incident debugging.
    """,

    verbose=True
)


def analyze_logs(logs):

    print("\n AI Incident Analysis\n")

    for log in logs:

        service = log["service"]
        severity = log["severity"]
        message = log["message"]

        if severity == "critical":

            print(f" CRITICAL issue detected in {service}")
            print(f"   {message}\n")

        elif severity == "high":

            print(f" HIGH severity incident in {service}")
            print(f"   {message}\n")

        else:

            print(f" MEDIUM issue in {service}")
            print(f"   {message}\n")