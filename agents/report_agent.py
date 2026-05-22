from crewai import Agent

from configs.llm_config import llm

report_agent = Agent(

    role="Incident Report Generator",

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

    verbose=True
)