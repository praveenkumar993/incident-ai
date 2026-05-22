from crewai import Agent

from configs.llm_config import llm

remediation_agent = Agent(

    role="Production Remediation Specialist",

    goal="""
    Suggest operational fixes
    and remediation strategies
    for production incidents
    """,

    backstory="""
    Senior DevOps engineer
    experienced in incident recovery,
    scaling strategies,
    and operational stabilization.
    """,

    llm=llm,

    verbose=True
)