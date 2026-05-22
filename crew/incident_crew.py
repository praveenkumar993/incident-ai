from crewai import Task, Crew

from agents.log_analysis_agent import (
    log_analysis_agent
)

from agents.root_cause_agent import (
    root_cause_agent
)

from agents.remediation_agent import (
    remediation_agent
)

from agents.report_agent import (
    report_agent
)


def run_incident_crew(logs):

    log_task = Task(

        description=f"""
        Analyze these production logs:

        {logs}

        Identify:
        - operational failures
        - severity
        - infrastructure impact
        """,

        agent=log_analysis_agent,

        expected_output="""
        Detailed production incident analysis
        """
    )

    root_cause_task = Task(

        description=f"""
        Identify probable root causes
        for these incidents:

        {logs}
        """,

        agent=root_cause_agent,

        expected_output="""
        Root cause investigation report
        """
    )

    remediation_task = Task(

        description=f"""
        Suggest remediation strategies
        for these incidents:

        {logs}
        """,

        agent=remediation_agent,

        expected_output="""
        Incident remediation plan
        """
    )

    report_task = Task(

        description="""
        Generate final incident report
        combining all investigations
        and remediation findings.
        """,

        agent=report_agent,

        expected_output="""
        Final structured incident report
        """
    )

    crew = Crew(

        agents=[
            log_analysis_agent,
            root_cause_agent,
            remediation_agent,
            report_agent
        ],

        tasks=[
            log_task,
            root_cause_task,
            remediation_task,
            report_task
        ],

        verbose=True
    )

    result = crew.kickoff()

    print("\n FINAL CREW OUTPUT\n")

    print(result)