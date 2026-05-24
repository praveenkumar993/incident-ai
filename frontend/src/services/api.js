import axios from "axios"

const API = axios.create({

  baseURL:
    import.meta.env.VITE_API_URL ||
    "http://localhost:8000"
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