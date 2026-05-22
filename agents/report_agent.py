from crewai import Agent

from configs.llm_config import llm

report_agent = Agent(

    role="incident report generator",

    goal="""
    Generate structured
    incident response reports
    """,

    backstory="""
    Expert technical documentation
    specialist for production incidents
    and operational reporting.
    """,

    llm=llm,
    allow_delegation=False,

    verbose=False
)