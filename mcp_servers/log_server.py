from fastapi import FastAPI

from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from crew.incident_crew import (
    run_incident_crew
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)
class IncidentRequest(BaseModel):

    incident_logs: list


@app.get("/logs")
def get_logs():

    return [
        {
            "service": "payment-service",
            "severity": "high",
            "message": "Database connection timeout"
        },
        {
            "service": "auth-service",
            "severity": "medium",
            "message": "Redis cache miss spike detected"
        },
        {
            "service": "gateway-service",
            "severity": "critical",
            "message": "CPU usage exceeded 95%"
        }
    ]


@app.post("/analyze")
def analyze_incident(request: IncidentRequest):

    result = run_incident_crew(
        request.incident_logs
    )

    final_report = str(result)

    final_report = final_report.replace(
        "[Date]",
        ""
    )

    final_report = final_report.replace(
        "[Time]",
        ""
    )

    final_report = final_report.replace(
        "[Environment]",
        ""
    )

    final_report = final_report.replace(
        "On ,",
        ""
    )

    return {
        "report": final_report
    }