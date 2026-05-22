from crewai import Agent

report_agent = Agent(

    role="Incident Report Generator",

    goal="""
    Generate structured production incident reports
    """,

    backstory="""
    Expert in incident documentation,
    operational reporting,
    and production event summarization.
    """,

    verbose=True
)


def generate_report(logs, root_causes, fixes):

    print("\n FINAL INCIDENT REPORT\n")

    print("INCIDENT LOGS:\n")

    for log in logs:

        print(
            f"- {log['service']} | "
            f"{log['severity']} | "
            f"{log['message']}"
        )

    print("\nROOT CAUSES:\n")

    for cause in root_causes:

        print(f"- {cause}")

    print("\nREMEDIATION ACTIONS:\n")

    for fix in fixes:

        print(f"- {fix}")