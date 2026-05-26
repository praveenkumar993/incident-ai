from fastapi import (
    FastAPI,
    UploadFile
)

from pydantic import BaseModel

from fastapi.middleware.cors import (
    CORSMiddleware
)

from crew.incident_crew import (
    run_incident_crew
)

from parsers.normalizer import (
    normalize_logs
)

from memory.vector_store import (

    store_incident_logs,

    search_similar_incidents
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

async def analyze_logs(file: UploadFile):

    content = await file.read()

    decoded_content = content.decode(
        "utf-8"
    )

    normalized_logs = normalize_logs(

        file.filename,

        decoded_content
    )

    store_incident_logs(
        normalized_logs
    )

    similar_incidents = []

    if normalized_logs:

        first_message = normalized_logs[0].get(

            "message",

            ""
        )

        similar_incidents = search_similar_incidents(

            first_message
        )

    result = run_incident_crew(
        normalized_logs
    )

    return {

        "normalized_logs":
            normalized_logs,

        "similar_incidents":
            similar_incidents,

        "report":
            str(result)
    }