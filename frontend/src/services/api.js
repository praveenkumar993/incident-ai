import axios from "axios"

const API = axios.create({
  baseURL: "http://127.0.0.1:8000"
})

export const analyzeIncident = async (logs) => {

  const response = await API.post(
    "/analyze",
    {
      incident_logs: logs
    }
  )

  return response.data
}