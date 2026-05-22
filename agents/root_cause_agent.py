from crewai import Agent

root_cause_agent = Agent(

    role="Root Cause Analyst",

    goal="""
    Identify the probable root cause of production incidents
    """,

    backstory="""
    Expert in debugging distributed systems,
    infrastructure bottlenecks,
    and production failures.
    """,

    verbose=True
)


def identify_root_cause(logs):

    findings = []

    for log in logs:

        message = log["message"]

        if "Database" in message:

            findings.append(
                "Possible database overload or connection pool exhaustion"
            )

        elif "CPU" in message:

            findings.append(
                "Possible infrastructure scaling issue causing high CPU utilization"
            )

        elif "Redis" in message:

            findings.append(
                "Possible cache instability or cache miss surge"
            )

    return findings