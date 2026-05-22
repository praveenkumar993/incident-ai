from crewai import Agent

remediation_agent = Agent(

    role="Incident Remediation Specialist",

    goal="""
    Suggest remediation actions for production incidents
    """,

    backstory="""
    Experienced DevOps engineer specializing
    in production recovery and infrastructure stabilization.
    """,

    verbose=True
)


def suggest_fixes(root_causes):

    fixes = []

    for cause in root_causes:

        if "database" in cause.lower():

            fixes.append(
                "Scale database replicas and increase connection pool"
            )

        elif "cpu" in cause.lower():

            fixes.append(
                "Scale application pods and investigate traffic spikes"
            )

        elif "cache" in cause.lower():

            fixes.append(
                "Restart Redis cache cluster and inspect cache hit ratio"
            )

    return fixes