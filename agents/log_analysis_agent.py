from crewai import Agent

from configs.llm_config import llm

log_analysis_agent = Agent(

    role="Senior Log Analysis Engineer",

    goal="""
    Analyze production incident logs
    and identify operational failures
    """,

    backstory="""
    Expert SRE engineer specializing
    in distributed systems,
    observability,
    and incident debugging.
    """,

    llm=llm,

    verbose=True
)