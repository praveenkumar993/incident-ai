from fastapi import FastAPI

app = FastAPI()

@app.get("/logs")
def get_logs():

    logs = [
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

    return {"incident_logs": logs}