from crewai import Agent

from configs.llm_config import llm

root_cause_agent = Agent(

    role="root cause investigator",

    goal="""
    Determine the root cause
    of production incidents
    """,

    backstory="""
    Infrastructure debugging expert
    specializing in production failures,
    scaling issues,
    and infrastructure bottlenecks.
    """,

    llm=llm,
    allow_delegation=False,

    verbose=False
)