from crewai import Task, Crew, Process

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
You are analyzing REAL production logs.

IMPORTANT RULES:
- ONLY use the provided logs
- DO NOT invent services
- DO NOT create fake incidents
- DO NOT hallucinate infrastructure
- ONLY analyze existing logs

Production Logs:
{logs}

For EACH log provide:
1. Service Name
2. Severity
3. Operational Issue
4. Infrastructure Impact
5. Business Impact

Return structured bullet points.
""",

        agent=log_analysis_agent,

        expected_output="""
        Detailed production incident analysis
        """
    )

    root_cause_task = Task(

        description=f"""
Investigate ONLY the provided logs.

IMPORTANT:
- Use ONLY provided log data
- Do NOT invent systems
- Do NOT create fake reports

Logs:
{logs}

For each incident identify:
1. Probable root cause
2. Why the issue happened
3. Affected infrastructure
4. Severity reasoning

Return structured analysis.
""",

        agent=root_cause_agent,

        expected_output="""
        Root cause investigation report
        """
    )

    remediation_task = Task(

        description=f"""
Based ONLY on the provided logs,
suggest production remediation steps.

Rules:
- No hallucinated systems
- No fake infrastructure
- Ground all suggestions in logs

Logs:
{logs}

For each incident provide:
1. Immediate fix
2. Long-term prevention
3. Infrastructure recommendation
4. Monitoring recommendation
""",

        agent=remediation_agent,

        expected_output="""
        Incident remediation plan
        """
    )

    report_task = Task(

        description="""
Generate FINAL incident report.

STRICT RULES:
- ONLY use outputs from previous agents
- DO NOT invent incidents
- DO NOT create fake services
- Keep report concise and structured
- NEVER use placeholders like [Date], [Time], [Service]
- If no timestamp exists in logs, omit dates completely

Required Sections:
1. Incident Summary
2. Root Causes
3. Severity Assessment
4. Remediation Actions
5. Infrastructure Impact
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
        process=Process.sequential,

        verbose=False
    )

    result = crew.kickoff()

    return result